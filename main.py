# main.py

from fastapi import FastAPI
from pydantic import BaseModel
from mylib import greet

app = FastAPI()

# Define a Pydantic model for the request body
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/lab")
async def lab():
    return {"message": "Lab goes here"}

@app.get("/greet/{name}")
async def read_item(name: str):
    return {"message": greet(name)}

# Define the POST endpoint
@app.post("/items/")
async def create_item(item: Item):
    return item  # Return the received item as a response