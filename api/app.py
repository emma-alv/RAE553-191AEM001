from flask import Flask
from flask_restful import Resource, Api
import json

Catalog = {}

app = Flask(__name__)
api = Api(app)

class Catalog(Resource):
    def get(self):
        app_json = json.dumps(Catalog)
        return app_json

class Item(Resource):
    def get(self, item_name):
        return Catalog[item_name]
    def post(selg, item_name):
        Catalog[item_name] = {'price': ''}

api.add_resource(Catalog, '/catalog') #http://127.0.0.1:5000/catalog/
api.add_resource(Item, '/item/<string:item_name>')
app.run(host = '0.0.0.0', port=5000)
