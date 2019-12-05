from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3

class Sinlge_Item(Resource):
    TABLE_NAME = 'items'

    def get_item(self, item_name):
        item = self.find_by_name(item_name)
        if item:
            return item
        else:
            not_item = {
                        'code': 404,
                        'message': 'Item {} not in the catalog'.format(item_name)
                        }, 404
            return not_item, 404

    def put_item(self, item_name, price):
        item = self.find_by_name(item_name)
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        if item:
            query = "UPDATE {table} SET price=? WHERE name=?".format(table=self.TABLE_NAME)
            result = cursor.execute(query, (price, item_name, ))
        else:
            query = "INSERT INTO {table} VALUES (?, ?)".format(table=self.TABLE_NAME)
            result = cursor.execute(query, (item_name, price, ))
        connection.commit()
        connection.close()
        item = self.find_by_name(item_name)
        return item
    
    def post_item(self, item_name, price):
        item = self.find_by_name(item_name)
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        if item:
            query = "UPDATE {table} SET price=? WHERE name=?".format(table=self.TABLE_NAME)
            result = cursor.execute(query, (price, item_name, ))         
            item = self.find_by_name(item_name)
            return item
        else:
            not_item = [{
                        'code': 404,
                        'message': 'Item {} not in the catalog'.format(item_name)
                        }, 404]
            return not_item


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
