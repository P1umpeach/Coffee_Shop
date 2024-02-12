from typing import List

from fastapi import HTTPException, APIRouter

from coffee.schemas import Coffee

router = APIRouter(
    prefix='/coffee',
    tags=['Base']
)


fake_coffee = [
    {"id": 1, "type": "Espresso", "volume": "1oz", "price": 2.50},
    {"id": 2, "type": "Cappuccino", "volume": "8oz", "price": 3.50},
    {"id": 3, "type": "Latte", "volume": "12oz", "price": 4.00},
    {"id": 4, "type": "Americano", "volume": "10oz", "price": 3.00}
]


@router.get("/coffee/{coffee_id}", response_model=List[Coffee])
def get_coffee(coffee_id: int):
    return [coffee for coffee in fake_coffee if coffee.get("id") == coffee_id]


@router.post("/coffee")
def add_coffee(coffee: List[Coffee]):
    fake_coffee.extend(coffee)
    return {"status": 200, "data": fake_coffee}


@router.delete("/coffee/{coffee_id}")
def delete_coffee(coffee_id: int):
    coffee = next((coffee for coffee in fake_coffee if coffee["id"] == coffee_id), None)
    if coffee is None:
        raise HTTPException(status_code=404, detail="Coffee not found")

    fake_coffee.remove(coffee)
    return {"message": "Coffee deleted successfully"}


