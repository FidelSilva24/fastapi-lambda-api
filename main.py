from fastapi import FastAPI
from storage import users_list, products_list
from mangum import Mangum



app = FastAPI()

@app.get("/")
async def root():
    return "Api Funcionando"


@app.get("/users")
async def users():
    return users_list


@app.get("/user/{id}")
async def user(id: int):
    result = next((u for u in users_list if u.id == id), None)
    if result:
        return result
    return {"message": "User not found"}

@app.get("/Products")
async def products():
    return products_list

@app.get("/product/{id}")
async def product(id: int):
    result = next((p for p in products_list if u.id == id), None)
    if result:
        return result
    return {"message": "product not found"}

handler = Mangum(app)