from flask import Flask, jsonify
from flask_restful import Resource, Api, abort, reqparse, request
from flask_jwt import JWT, jwt_required, current_identity
from security import authenticate, identity

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'fS%JG@Pe8^4fYDMV'
app.config['JWT_AUTH_URL_RULE'] = '/login'
jwt = JWT(app, authenticate, identity)

items = {"item_1": {"id": 1, "price": 100},
         "item_2": {"id": 2, "price": 200}
         }

@jwt.jwt_error_handler
def customized_error_handler(error):
    return jsonify({
                    'message'   : error.description,
                    'code'      : error.status_code
                    }), error.status_code

def abort_if_item_doesnt_exist(item_name):
    if item_name not in items:
        return jsonify({
                        'code': 404,
                        'message': 'Item {} not in the catalog'.format(item_name)
                        }), 404

@app.route('/items', methods=['GET'])
@jwt_required()
def Items():
    if request.method == 'GET':
        list_items = [i for i in items.keys()]
        return jsonify({
                        'Items': list_items}), 201    


@app.route('/item', methods=['GET','PUT','POST','DELETE'])
@jwt_required()
def Item():
    item_name = request.args.get('item_name')
    if request.method == 'PUT':
        if item_name in items.keys():
            id = items[item_name]['id']
        else:
            id = len(items.keys()) + 1
        parser = reqparse.RequestParser()
        parser.add_argument("price")
        args = parser.parse_args()
        items[item_name] = {"id": id, "price": args["price"]}
        return jsonify({
                        'code': 201,
                        'message': "Item {} succesfull updated".format(item_name)
                        }), 201
    if item_name not in items:
        return jsonify({
                        'code': 404,
                        'message': 'Item {} not in the catalog'.format(item_name)
                        }), 404    
    if request.method == 'GET':
        return jsonify({
            item_name: items[item_name]
            }), 201
    if request.method == 'POST':
        parser = reqparse.RequestParser()
        parser.add_argument("price")
        args = parser.parse_args()
        items[item_name]["price"] = args["price"]
        return jsonify({
                        'code': 201,
                        'message': "Item {} succesfull updated".format(item_name)
                        }), 201
    if request.method == 'DELETE':
        items.pop(item_name)
        return jsonify({
                        'code': 201,
                        'message': "Item {} succesfull deleted".format(item_name)
                        }), 201



#api.add_resource(Items, '/items') 
#api.add_resource(Item, '/item/<string:item_name>')
#api.add_resource(Auth, '/auth')

if __name__ == '__main__':
    app.run(port=5000)
