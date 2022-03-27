from typing import Dict, List

from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
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
    """Endpoint from Bite 03"""
    foods[food.id] = food
    return food


@app.get("/", response_model=List[Food])
async def read_foods():
    """Endpoints from Bite 04"""
    return list(foods.values())


@app.get("/{food_id}", response_model=Food)
async def read_food(food_id: int):
    """Endpoints from Bite 04"""
    return foods[food_id]


@app.put("/{food_id}", response_model=Food)
async def update_food(food_id: int, food: Food):
    if food_id in foods.keys():
        update_food_encoded = jsonable_encoder(food)
        foods[food_id] = update_food_encoded
    else:
        raise HTTPException(status_code=404, detail="Food not found")
    return update_food_encoded


@app.delete("/{food_id}")
def delete_food(food_id: int):
    if food_id in foods.keys():
        del foods[food_id]
    else:
        raise HTTPException(status_code=404, detail="Food not found")
    return {"ok": True}
