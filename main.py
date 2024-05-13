from fastapi import FastAPI, HTTPException, Depends
from database_operations import get_db
from sqlalchemy import func
from sqlalchemy.orm import Session
from models import Item as DBItem
from schemas import Item as ItemSchema


app = FastAPI()


@app.get('/items', response_model=list[ItemSchema])
def view_items(db: Session = Depends(get_db)):
    items = db.query(DBItem).all()
    return items



@app.post("/items/", response_model=ItemSchema) 
def create_item(item: ItemSchema, db: Session = Depends(get_db)):
    db_item = DBItem(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@app.get("/items/{item_name}") 
def read_item(item_name: str, db: Session = Depends(get_db)):
    item = db.query(DBItem).filter(DBItem.name == item_name).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.put("/items/{item_name}") 
def update_item(item_name: str, item_data: ItemSchema, db: Session = Depends(get_db)):
    item = db.query(DBItem).filter(DBItem.name == item_name).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    for field, value in item_data.model_dump().items():
        setattr(item, field, value)
    db.commit()
    return item

@app.delete("/items/{item_name}") 
def delete_item(item_name: str, db: Session = Depends(get_db)):
    item = db.query(DBItem).filter(DBItem.name == item_name).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()
    return {"message": "Item deleted successfully"}

@app.get("/total_cost") 
def get_total_cost(db: Session = Depends(get_db)):
    total_cost = db.query(func.sum(DBItem.price)).scalar()
    if total_cost is None:
        total_cost = 0
    return {"total_cost": total_cost}