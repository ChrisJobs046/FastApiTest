from fastapi import FastAPI
from pydantic import BaseModel

db = []

class City(BaseModel):
    name = str
    country: str
    timezone: str

app = FastAPI()

@app.get("/")
def Index():
    return { 'key': 'value' }

app.get("/cities")
def get_city():
    return db


#@app.get("/cities/{city_id}")

@app.pos("/cities")
def create_city(city: City):
    db.append(city.dict())
    return db[-1]

@app.delete("/cities/{city_id}")
def delete_city(city_id: int):
    db.pop(city_id - 1) #esto es para salir de la base de datos en memoria y que lo haga desde 1 y no a partir de 0
    return {} #db


#@app.put("/cities/{city_id}")

#@app.get("/items/{item_id}")

