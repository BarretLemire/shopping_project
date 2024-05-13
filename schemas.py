from pydantic import BaseModel
#from sqlalchemy import Column, Integer, String, Float
#from database_operations import Base

class Item(BaseModel):
    name: str 
    quantity: int
    type: str
    brand: str
    color: str
    price: float


#api schemas