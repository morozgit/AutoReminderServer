from pydantic import BaseModel


class CarParts(BaseModel):
    part_id: int
    part_name: str
    price: int


class CarMileage(BaseModel):
    mileage: int
