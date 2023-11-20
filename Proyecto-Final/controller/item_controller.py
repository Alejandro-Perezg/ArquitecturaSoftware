import psycopg2
from flask import request, jsonify

from repository.item_repository import ItemRepository


connection = psycopg2.connect("host=localhost dbname=final user=jvnko password=my_password")
item_repository = ItemRepository(connection)

class ItemController:

    def __init__(self, item_repository):
        self.item_repository = item_repository
        
    def changeCurrency(self, sku, currency):
        item = self.item_repository.getItem(sku)
        if item:
            exchange_rate_url = f"http://api.exchangeratesapi.io/v1/latest?access_key=YOUR_ACCESS_KEY&symbols={currency}"
            response = request.get(exchange_rate_url)
            exchange_rate_data = response.json()

            exchange_rate = exchange_rate_data["rates"].get(currency, 1.0)
            converted_price = item["price"] * exchange_rate

            json_item = {
                "sku": item["sku"],
                "name": item["name"],
                "description": item["description"],
                "price": str(converted_price),
                "quantity": item["quantity"],
                "expdate": str(item["expdate"])
            }
            return jsonify(json_item)
        else:
            return 'Item not found'


    def getItems(self):
        items = self.item_repository.getItems()
        json_items = []
        for item in items:
            json_item = {
                "sku": item["sku"],
                "name": item["name"],
                "description": item["description"],
                "price": str(item["price"]),
                "quantity": item["quantity"],
                "expdate": str(item["expdate"])
            }
            json_items.append(json_item)

        return jsonify(json_items)
    
    def getItem(self, sku):
        item = self.item_repository.getItem(sku)
        if item:
            json_item = {
                "sku": item["sku"],
                "name": item["name"],
                "description": item["description"],
                "price": item["price"],
                "quantity": item["quantity"],
                "expdate": str(item["expdate"])
            }
            return jsonify(json_item)
        else:
            return 'Item not found'

    def add_item(self):
        item_data = request.get_json()
        self.item_repository.add_item(item_data)
        return 'Item added successfully'

    def deleteItem(self, sku):
        self.item_repository.deleteItem(sku)
        return 'Item deleted successfully'



