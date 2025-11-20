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
    users = filter(lambda user: user.id == id, users_list)  # type: ignore
    try:
        return list(users)[0]
    except:
        return ""

@app.get("/Products")
async def products():
    return products_list

handler = Mangum(app)