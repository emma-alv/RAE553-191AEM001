from flask import Flask
from flask_restful import Resource, Api, abort

app = Flask(__name__)
api = Api(app)

items = {"items": ["item_1", "item_2"],
         "item_1": {"id": 1, "price": 100},
         "item_2": {"id": 2, "price": 200}
         }

def abort_if_item_doesnt_exist(item_name):
    if item_name not in items:
        abort(404, message="Item {} doesn't exist".format(item_name))

class Items(Resource):
    def get(self):
        return items["items"]

class Item(Resource):
    def get(self, item_name):
        abort_if_item_doesnt_exist(item_name)
        return items[item_name]
    def post(selg, item_name):
        if item_name in items['items']:
            id = items[item_name]['id']
        else:
            id = len(items["items"]) + 1
            items['items'].append(item_name)
        items[item_name] = {"id": id, "price": ""}
        return "Item {} succesfull added".format(item_name)

api.add_resource(Items, '/items') # http://127.0.0.1:5000/items/
api.add_resource(Item, '/item/<string:item_name>') # http://127.0.0.1:5000/item/≤item_name>

app.run(port=5000)
