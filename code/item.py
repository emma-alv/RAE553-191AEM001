from flask_restful import Resource
import sqlite3

class List_Items(Resource):
    TABLE_NAME = 'items'
    def get_items(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM {table}".format(table=self.TABLE_NAME)
        result = cursor.execute(query)
        row = cursor.fetchall()
        catalog = {}
        for item in row:
            catalog[item[0]] = {"name": item[0], "price": item[1]}
        return catalog 

class Sinlge_Item(Resource):
    TABLE_NAME = 'items'

    def get_item(self, item_name):
        item = self.find_by_name(item_name)
        if item:
            return item

    def put_item(self, item_name, price):
        item = self.find_by_name(item_name)
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        if item:
            query = "UPDATE {table} SET price=? WHERE name=?".format(table=self.TABLE_NAME)
            cursor.execute(query, (price, item_name, ))
        else:
            query = "INSERT INTO {table} VALUES (?, ?)".format(table=self.TABLE_NAME)
            cursor.execute(query, (item_name, price, ))
        connection.commit()
        connection.close()
        item = self.find_by_name(item_name)
        return item
    
    def post_item(self, item_name, price):
        item = self.find_by_name(item_name)
        if item:
            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()
            query = "UPDATE {table} SET price=? WHERE name=?".format(table=self.TABLE_NAME)
            cursor.execute(query, (price, item_name, ))         
            item = self.find_by_name(item_name)
            connection.commit()
            connection.close()
            item = self.find_by_name(item_name)
            return item

    def delete_item(self, item_name):
        item = self.find_by_name(item_name)
        if item:
            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()
            query = "DELETE FROM {table} WHERE name=?".format(table=self.TABLE_NAME)
            cursor.execute(query, (item_name,))
            connection.commit()
            connection.close()
            return {"message": "Item deleted"}

    @classmethod
    def find_by_name(cls, item_name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table} WHERE name=?".format(table=cls.TABLE_NAME)
        result = cursor.execute(query, (item_name,))
        row = result.fetchone()
        connection.close()
        if row:
            return {"item": {"name": row[0], "price": row[1]}}
