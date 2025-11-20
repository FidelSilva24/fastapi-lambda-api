from pydantic import BaseModel

class User(BaseModel):
    name: str
    surname: str
    email: str
    age: int
    id: int

class Product(BaseModel):
    name: str
    brand: str
    price: float
    id: int