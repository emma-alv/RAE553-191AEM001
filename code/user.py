import sqlite3
from flask import jsonify
from flask_restful import Resource, reqparse

class User(object):
    def __init__(self, id, username, password):
        self.id         = id
        self.username   = username
        self.password   = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None
        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else: 
            user = None
        connection.close()
        return user

class UserRegister(object):
    def __init__(self, id, username, password):
        self.id         = id
        self.username   = username
        self.password   = password

    @classmethod
    def new_user(cls, username, password):
        if User.find_by_username(username):
            return "A user with this username already exists"

        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "INSERT INTO users VALUES (NULL, ?, ?)"
        cursor.execute(query, (username, password,))

        connection.commit()
        connection.close()

        return "User created successfully."
