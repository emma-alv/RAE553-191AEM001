from flask import Flask
from flask_restful import Resource, Api, abort

app = Flask(__name__)
api = Api(app)

Items = {"items": []}

def abort_if_item_doesnt_exist(item_name):
    if item_name not in Items:
        abort(404, message="Item {} doesn't exist".format(item_name))

class Catalog(Resource):
    def get(self):
        return Items

class Item(Resource):
    def get(self, item_name):
        abort_if_item_doesnt_exist(item_name)
        return Items[item_name]
    def post(selg, item_name):
        Items['items'].append(item_name)
        Items[item_name] = {'price': ''}
        return "Item {} succesfull added".format(item_name)

api.add_resource(Catalog, '/items') # http://127.0.0.1:5000/Items/
api.add_resource(Item, '/item/<string:item_name>') # http://127.0.0.1:5000/item/≤item_name>

app.run(port=5000)
