from datetime import datetime
from typing import Any, Dict

from fastapi import FastAPI, HTTPException
from passlib.context import CryptContext
from pydantic import BaseModel

from fastapi.testclient import TestClient

# https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
# We'll explore further in a later Bite
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

LAME_PASSWORD = "1234"  # noqa S105
AVG_HUMAN_CALORIES_PER_DAY = 2250


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
    max_daily_calories: int = AVG_HUMAN_CALORIES_PER_DAY

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


@app.post("/", status_code=201)
async def create_food_entry(entry: FoodEntry):
    if entry.id in food_log:
        raise HTTPException(status_code=400, detail="Food entry already logged, use an update request")
    else:
        # get consumed total so far for user
        consumed_calories = sum([v.total_calories for v in food_log.values() if v.user.id == entry.user.id])
        # get consumption with new food
        new_calories = entry.total_calories
        # add to food log if new calories do not exceed max
        if consumed_calories+new_calories <= entry.user.max_daily_calories:
            food_log[entry.id] = entry
        else:
            raise HTTPException(status_code=400, detail=f"Cannot add more food than daily caloric allowance = {entry.user.max_daily_calories} kcal / day")
    return entry


# if __name__ == '__main__':
#     main()
#
# def main():
#     print('thank you for looking after Mama and Naia')
#
#     user = dict(id=1, username="user", password=LAME_PASSWORD)
#
#     food = dict(
#         id=1,
#         name="egg",
#         serving_size="piece",
#         kcal_per_serving=78,
#         protein_grams=6.2,
#         fibre_grams=0,
#     )
#     food_entry1 = dict(id=1, user=user, food=food, number_servings=1.5)
#
#     client = TestClient(app)
#     client.post("/", json=food_entry1)
#
#     food_entry2 = dict(id=2, user=user, food=food, number_servings=26.5)
#     resp = client.post("/", json=food_entry2)
#
#     print(food_log)
#
#     food_entry3 = food_entry1.copy()
#     food_entry3["id"] = 3
#     food_entry3["number_servings"] = 1
#     resp = client.post("/", json=food_entry3)
#
#     print(food_log)
