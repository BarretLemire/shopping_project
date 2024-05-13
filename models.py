from sqlalchemy import Column, Integer, String, Float
from database_operations import Base




class Item(Base):
    __tablename__ = 'items'
    
    name = Column(String, primary_key=True)
    quantity = Column(Integer)
    type = Column(String)
    brand = Column(String)
    color = Column(String)
    price = Column(Float)

#database models