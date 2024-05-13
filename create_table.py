import json
from database_operations import Session
from models import Item

with open('cart.json', 'r') as f:
    cart_data = json.load(f)

session = Session()


for item_data in cart_data['items']:
    item = Item(**item_data)
    session.add(item)

session.commit()

session.close()