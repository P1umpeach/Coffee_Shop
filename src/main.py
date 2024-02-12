from typing import List
from pydantic import BaseModel, Field

from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="Coffee shop"
)

fake_coffee = [
    {"id": 1, "type": "Espresso", "volume": "1oz", "price": 2.50},
    {"id": 2, "type": "Cappuccino", "volume": "8oz", "price": 3.50},
    {"id": 3, "type": "Latte", "volume": "12oz", "price": 4.00},
    {"id": 4, "type": "Americano", "volume": "10oz", "price": 3.00}
]


class Coffee(BaseModel):
    id: int
    type: str = Field(max_length=10)
    volume: str
    price: float = Field(ge=0)


@app.get("/coffee/{coffee_id}", response_model=List[Coffee])
def get_coffee(coffee_id: int):
    return [coffee for coffee in fake_coffee if coffee.get("id") == coffee_id]


@app.post("/coffee")
def add_coffee(coffee: List[Coffee]):
    fake_coffee.extend(coffee)
    return {"status": 200, "data": fake_coffee}


@app.delete("/coffee/{coffee_id}")
def delete_coffee(coffee_id: int):
    coffee = next((coffee for coffee in fake_coffee if coffee["id"] == coffee_id), None)
    if coffee is None:
        raise HTTPException(status_code=404, detail="Coffee not found")

    fake_coffee.remove(coffee)
    return {"message": "Coffee deleted successfully"}


