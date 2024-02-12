from pydantic import BaseModel, Field


class Coffee(BaseModel):
    id: int
    type: str = Field(max_length=10)
    volume: str
    price: float = Field(ge=0)


