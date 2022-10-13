import imp
from msilib.schema import tables
# from typing_extensions import Required
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_restful import Resource, Api, reqparse, abort, fields
from flask_mongoengine import MongoEngine
from datetime import datetime
from mongoengine import *
from flask_pymongo import PyMongo
import json
import os
app = Flask(__name__)
main = Api(app)
app.config['MONGODB_SETTINGS'] = {
    'db': 'pizza_house',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)

class Order(db.Document):
    # id = db.IntField(primary_key=True)
    order = db.ListField(required=True)
    
    def __repr__(self):
        return 'Order '+str(self.order)
orders = {"order": ["Pizza1", "Pizza2"]}


order_post_args = reqparse.RequestParser()
order_post_args.add_argument("order", type=list, help="order is required", required=True)
    

# print(order_post_args["order"])
@app.route('/welcome')
def base():
    return '<h1>Welcome to Pizza House</h1>'

@app.route('/order')
def orderdetails():
    # request_data = request.get_json()
    args = {"order":["MediumPizza", "LargePizza"]}
    order = Order(order=args["order"]).save()
    return jsonify(order)
li = []
@app.route('/getorders')
def getorders():
    for order in Order.objects():
        li.append(order)
    return jsonify(li)

# @app.route('/getorders')
if __name__ == "__main__":
    app.run(debug=True)