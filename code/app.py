from flask import Flask, jsonify
from flask_restful import Resource, Api, abort, reqparse, request
from flask_jwt import JWT, jwt_required, current_identity
from security import authenticate, identity
from user import UserRegister
from item import Sinlge_Item

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
    item = Sinlge_Item()
    item_name = request.args.get('item_name')
    parser = reqparse.RequestParser()
    parser.add_argument("price")
    args = parser.parse_args()
    if request.method == 'PUT':
        item_requested = item.put_item(item_name, args["price"])
        return item_requested   
    if request.method == 'GET':
        item_requested = item.get_item(item_name)
        # if item_requested:
        #     return item_requested
        return item_requested
    if request.method == 'POST':
        parser = reqparse.RequestParser()
        parser.add_argument("price")
        args = parser.parse_args()
        item_requested = item.post_item(item_name, price)
        return jsonify(item_requested)
    if request.method == 'DELETE':
        items.pop(item_name)
        return jsonify({
                        'code': 201,
                        'message': "Item {} succesfull deleted".format(item_name)
                        }), 201

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
