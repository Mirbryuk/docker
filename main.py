from typing import Union
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def root_action():
    return {"surname": "Бирюк", "name": "Мария", "patronymic": "Денисовна"}

@app.get("/users")
def users_action():
    return {"phone_number": "89831084548", "email": "mashamirbryuk@gmail.com"}

@app.get("/tools")
def users_action():
    return {"info": " Я сделала простое API, используя FastAPI и Docker"}