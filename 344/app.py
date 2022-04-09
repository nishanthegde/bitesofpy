from datetime import datetime
from typing import Any, Dict, List

from fastapi import FastAPI, Request
from fastapi.testclient import TestClient
from fastapi.responses import HTMLResponse
from passlib.context import CryptContext
from pydantic import BaseModel

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)


class Food(BaseModel):
    id: int
    name: str
    serving_size: str
    kcal_per_serving: int
    protein_grams: float
    fibre_grams: float = 0


class User(BaseModel):
    id: int
    username: str
    password: str

    def __init__(self, **data: Any):
        data["password"] = get_password_hash(data["password"])
        super().__init__(**data)


class FoodEntry(BaseModel):
    id: int
    user: User
    food: Food
    date_added: datetime = datetime.now()
    number_servings: float

    @property
    def total_calories(self):
        return self.food.kcal_per_serving * self.number_servings


app = FastAPI()

food_log: Dict[int, FoodEntry] = {}

LAME_PASSWORD = "1234"  # noqa S105

HTML_TEMPLATE = """<!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Food log for {username}</title>
</head>

<body>
    <table>
        <thead>
            <th>Food</th>
            <th>Added</th>
            <th>Servings</th>
            <th>Calories (kcal)</th>
        </thead>
        <tbody>
            {table_rows}
        </tbody>
    </table>

</body>
</html>"""
TABLE_ROW = """<tr>
    <td>{food_name}</td>
    <td>{date_added}</td>
    <td>{number_servings} x {serving_size}</td>
    <td>{total_calories}</td>
</tr>"""


@app.post("/", status_code=201)
async def create_food_entry(entry: FoodEntry):
    """Previous Bite and used in test"""
    food_log[entry.id] = entry
    return entry


@app.get("/{username}", response_class=HTMLResponse, status_code=200)
async def show_foods_for_user(request: Request, username: str):
    # 1. extract foods for user using the food_log dict
    # 2. build up the embedded html string
    # 3. return an HTMLResponse (with the html content and status code 200)
    food_entries = []
    table_row_entries = []
    table_rows = ''

    for v in food_log.values():
        if v.user.username == username:
            table_row_entries.append(TABLE_ROW.format(food_name=v.food.name,
                                                      date_added=datetime.strftime(v.date_added, "%Y-%m-%d %H:%M:%S.%f")
                                                      , number_servings=v.number_servings,
                                                      serving_size=v.food.serving_size,
                                                      total_calories=v.total_calories))
    # print(table_row_entries)

    for row in table_row_entries:
        table_rows += row

    return HTML_TEMPLATE.format(username=username, table_rows=table_rows)


# def main():
#     print('thank you for looking after Mama and Naia!')
#
#     user = dict(id=1, username="Julian", password=LAME_PASSWORD)
#
#     food1 = dict(
#         id=1,
#         name="egg",
#         serving_size="piece",
#         kcal_per_serving=78,
#         protein_grams=6.2,
#         fibre_grams=0,
#     )
#     food_entry1 = dict(id=1, user=user, food=food1, number_servings=1.5)
#
#     food2 = dict(
#         id=2,
#         name="oatmeal",
#         serving_size="100 grams",
#         kcal_per_serving=336,
#         protein_grams=13.2,
#         fibre_grams=10.1,
#     )
#     food_entry2 = dict(id=2, user=user, food=food2, number_servings=2)
#
#     client = TestClient(app)
#
#     client.post("/", json=food_entry1)
#     client.post("/", json=food_entry2)
#
#     print(food_log)
#
#     resp = client.get("/Julian")
#     # print(resp)
#
#
# if __name__ == '__main__':
#     main()
