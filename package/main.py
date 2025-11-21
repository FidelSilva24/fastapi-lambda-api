from fastapi import FastAPI, Depends
from storage import users_list, products_list
from mangum import Mangum
from auth import verify_token



app = FastAPI()

@app.get("/")
async def root():
    return "Api Funcionando"


@app.get("/users")
async def users(payload: dict = Depends(verify_token)):
    return users_list


@app.get("/user/{id}")
async def user(id: int, payload: dict = Depends(verify_token)):
    result = next((u for u in users_list if u.id == id), None)
    if result:
        return result
    return {"message": "User not found"}

@app.get("/Products")
async def products():
    return products_list

@app.get("/product/{id}")
async def product(id: int):
    result = next((p for p in products_list if p.id == id), None)
    if result:
        return result
    return {"message": "product not found"}

handler = Mangum(app)