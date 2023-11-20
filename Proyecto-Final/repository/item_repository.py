import psycopg2
from flask import request

class ItemRepository:
    def __init__(self, connection):
        self.connection = connection

    def load_items(self):
        query = "SELECT * FROM my_schema.items"
        items = self._execute_query(query)
        return [self._row_to_dict(row) for row in items]

    def get_items(self):
        return self.load_items()
    
    def get_item(self, sku):
        query = "SELECT * FROM my_schema.items WHERE sku=%s"
        values = (sku,)
        row = self._execute_query(query, values, fetchone=True)
        return self._row_to_dict(row) if row else None

    def add_item(self, item):
        query = "INSERT INTO my_schema.items (sku, name, description, price, quantity, expdate) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (item["sku"], item["name"], item["description"], item["price"], item["quantity"], item["expdate"])
        self._execute_query(query, values)
        self.connection.commit()
        return "Item added"

    def delete_item(self, sku):
        query = "DELETE FROM my_schema.items WHERE sku=%s"
        values = (sku,)
        self._execute_query(query, values)
        self.connection.commit()
        return "Item removed"



    def _execute_query(self, query, values=None, fetchone=False):
        with self.connection.cursor() as cursor:
            cursor.execute(query, values)
            if fetchone:
                return cursor.fetchone()
            else:
                return cursor.fetchall()

    def _row_to_dict(self, row):
        if row:
            return {
                "sku": row[0],
                "name": row[1],
                "description": row[2],
                "price": row[3],
                "quantity": row[4],
                "expdate": row[5]
            }
        else:
            return None
