from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pydantic import BaseModel
from typing import List

app = FastAPI()

client = MongoClient("mongodb://localhost:27017/")
db = client.my_database
collection = db.my_collection

class Item(BaseModel):
    name: str
    email: str

@app.post("/users/", response_model=Item)
async def create_users(item: Item):
    result = collection.insert_one(item.dict())
    if result.inserted_id:
        return item
    raise HTTPException(status_code=400, detail="Item not created")


@app.get("/users/", response_model=List[Item])
async def read_users():
    items = list(collection.find({}, {'_id': 0}))
    return items


@app.get("/names/", response_model=List[Item])
async def read_names(name :str):
    items = list(collection.find({'name' : name}, {'_id': 0}))
    return items

@app.put("/update_using_names",response_model=List[Item])
async def update_names(name : str,item : Item):
    items = collection.replace_one({'name' : name} , item.dict())
    if items.modified_count == 1:
        return item
    raise HTTPException(status_code=404, detail="Item not found or not modified")


@app.delete("/delete_using_names",response_model=List[Item])
async def delete_names(name : str,item : Item):
    items = collection.delete_one({'name' : name})
    if items.deleted_count == 1:
        return item
    raise HTTPException(status_code=404, detail="Item not found or not deleted")