from typing import Dict

from fastapi import FastAPI
from pydantic import BaseModel


class Food(BaseModel):
    """Model from Bite 02"""

    id: int
    name: str
    serving_size: str
    kcal_per_serving: int
    protein_grams: float
    fibre_grams: float = 0


app = FastAPI()
foods: Dict[int, Food] = {}


@app.post("/", status_code=201)
async def create_food(food: Food):
    foods[food.id] = food
    return food


@app.get("/", status_code=200)
async def read_foods():
    ret = []
    for v in foods.values():
        ret.append(v)

    return ret


@app.get("/{food_id}", status_code=200)
async def read_food(food_id: int):
    return foods[food_id]
