from flask import Flask
from flask_restful import Resource, Api, abort, reqparse

app = Flask(__name__)
api = Api(app)

items = {"item_1": {"id": 1, "price": 100},
         "item_2": {"id": 2, "price": 200}
         }

def abort_if_item_doesnt_exist(item_name):
    if item_name not in items:
        abort(404, message="Item {} doesn't exist".format(item_name))

class Items(Resource):
    def get(self):
        list_items = [i for i in items.keys()]
        return list_items, 201

class Item(Resource):
    def get(self, item_name):
        abort_if_item_doesnt_exist(item_name)
        return items[item_name], 201
    def put(self, item_name):
        if item_name in items.keys():
            id = items[item_name]['id']
        else:
            id = len(items.keys()) + 1
        parser = reqparse.RequestParser()
        parser.add_argument("price")
        args = parser.parse_args()
        items[item_name] = {"id": id, "price": args["price"]}
        return "Item {} succesfull created".format(item_name), 201
    def post(self, item_name):
        if item_name in items.keys():
            parser = reqparse.RequestParser()
            parser.add_argument("price")
            args = parser.parse_args()
            items[item_name]["price"] = args["price"]
            return "Item {} succesfull updated".format(item_name), 201
        else:
            abort_if_item_doesnt_exist(item_name)
            return
    def delete(self, item_name):
        if item_name in items.keys():
            items.pop(item_name)
            return "Item {} succesfull deleted".format(item_name), 201
        else:
            abort_if_item_doesnt_exist(item_name)
            return



api.add_resource(Items, '/items') 
api.add_resource(Item, '/item/<string:item_name>') 

app.run(port=5000)
