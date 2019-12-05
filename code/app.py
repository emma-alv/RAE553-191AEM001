from flask import Flask, jsonify
from flask_restful import Resource, Api, abort, reqparse, request
from flask_jwt import JWT, jwt_required, current_identity
from security import authenticate, identity
from user import UserRegister
from item import Sinlge_Item, List_Items

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'fS%JG@Pe8^4fYDMV'
app.config['JWT_AUTH_URL_RULE'] = '/login'
jwt = JWT(app, authenticate, identity)

@jwt.jwt_error_handler
def customized_error_handler(error):
    return jsonify({
                    'message'   : error.description,
                    'code'      : error.status_code
                    }), error.status_code

def error_item_not_found(item_name):
    return jsonify({
            'code': 404,
            'message': 'Item {} not in the catalog'.format(item_name)
            })

@app.route('/items', methods=['GET'])
@jwt_required()
def Items():
    items = List_Items()
    if request.method == 'GET':
        items = items.get_items()
        if items:
            return jsonify(items), 201
        return jsonify({
            "message": "Empty Catalog"
        }), 404


@app.route('/item', methods=['GET','PUT','POST','DELETE'])
@jwt_required()
def Item():
    item = Sinlge_Item()
    item_name = request.args.get('item_name')
    parser = reqparse.RequestParser()
    parser.add_argument("price")
    args = parser.parse_args()
    
    if request.method == 'PUT':
        item_requested = item.put_item(item_name, args["price"])
        return item_requested, 201   
    
    if request.method == 'GET':
        item_requested = item.get_item(item_name)
        if item_requested:
            return item_requested, 201
        return error_item_not_found(item_name), 404
    
    if request.method == 'POST':
        item_requested = item.post_item(item_name, args["price"])
        if item_requested:
            return item_requested, 201
        return error_item_not_found(item_name), 404
    
    if request.method == 'DELETE':
        item_requested = item.delete_item(item_name)
        if item_requested:
            return item_requested, 201
        return error_item_not_found(item_name), 404

@app.route('/signin', methods=['POST'])
def Sigin():
    if request.method == 'POST':
        parser = reqparse.RequestParser()
        parser.add_argument("username",
            type=str,
            required=True,
            help="This field cannot be blank"
        )
        parser.add_argument("password",
            type=str,
            required=True,
            help="This field cannot be blank"
        )
        data = parser.parse_args()
        create_user = UserRegister.new_user(data["username"], data["password"])
        return jsonify({
            "message": create_user
            }), 201

if __name__ == '__main__':
    app.run(port=5000)
