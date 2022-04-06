from datetime import datetime
from typing import Any, Dict, List

from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
from fastapi.encoders import jsonable_encoder
from passlib.context import CryptContext
from pydantic import BaseModel

# https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
# We'll export authentication further in a later Bite

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

LAME_PASSWORD = "1234"  # noqa S105


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


@app.post("/", status_code=201)
async def create_food_entry(food_entry: FoodEntry):
    food_log[food_entry.id] = food_entry
    return food_entry


@app.get("/{user_id}", response_model=List[FoodEntry])
async def get_foods_for_user(user_id: int):
    food_entries = []
    for v in food_log.values():
        if v.user.id == user_id:
            food_entries.append(v)

    return food_entries


@app.delete("/{food_entry_id}")
def delete_food_entry(food_entry_id: int):
    if food_entry_id in food_log.keys():
        del food_log[food_entry_id]
    else:
        raise HTTPException(status_code=404, detail="Food entry not found")
    return {"ok": True}


@app.put("/{food_entry_id}", response_model=FoodEntry)
async def update_food_entry(food_entry_id: int, food_entry: FoodEntry):
    if food_entry_id in food_log.keys():
        # update_food_entry_encoded = jsonable_encoder(food_entry)
        food_log[food_entry_id] = food_entry # update_food_entry_encoded
    else:
        raise HTTPException(status_code=404, detail="Food entry not found")
    return food_entry


# We've hidden the previous Food CRUD to keep it compact and to force you to
# repeat the API building process (deliberate practice is key!)

# Create CRUD endpoints for FoodEntry below as per instructions in the Bite ...
# def main():
#     print('Thank you for looking after Mama and Naia')
#
#     user1 = dict(id=1, username="user1", password=LAME_PASSWORD)
#     user2 = dict(id=2, username="user2", password=LAME_PASSWORD)
#
#     food1 = dict(
#         id=1,
#         name="egg",
#         serving_size="piece",
#         kcal_per_serving=78,
#         protein_grams=6.2,
#         fibre_grams=0,
#     )
#
#     food2 = dict(
#         id=2,
#         name="oatmeal",
#         serving_size="100 grams",
#         kcal_per_serving=336,
#         protein_grams=13.2,
#         fibre_grams=10.1,
#     )
#
#     client = TestClient(app)
#
#     payload1 = dict(id=1, user=user1, food=food1, number_servings=1.5)
#     client.post("/", json=payload1)
#     payload2 = dict(id=2, user=user2, food=food2, number_servings=2.2)
#     client.post("/", json=payload2)
#
#     entry = client.get("/1").json()[0]
#     print(food_log)
#     # for v in food_log.values():
#     #     if v.user.id == 1:
#     #         print(v)
#
#     # print(entry["number_servings"])
#     new_entry = entry.copy()
#     new_entry["number_servings"] = 3
#     client.put(f"/{entry['id']}", json=new_entry)
#     print(food_log)
#
#
# if __name__ == '__main__':
#     main()
