from ast import arg
from crypt import methods
import imp
from msilib.schema import tables
import re
import redis
import cli.app
import time
from rq import Queue, Connection, Worker
from rq import Queue
from flask import Flask, render_template, request, redirect, url_for, jsonify, current_app
from flask_restful import Resource, Api, reqparse, abort, fields
from flask_mongoengine import MongoEngine
from datetime import datetime
from flask.cli import with_appcontext
from mongoengine import *
from celery import Celery
import time
from celery.utils.log import get_task_logger
from flask_pymongo import PyMongo
import json
from worker import *
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
    order = db.ListField(required=True)
    
    def __repr__(self):
        return 'Order '+str(self.order)
orders = {"order": ["Pizza1", "Pizza2"]}


order_post_args = reqparse.RequestParser()
order_post_args.add_argument("order", type=list, help="order is required", required=True)
    

# Welcome API
@app.route('/welcome')
def base():
    return '<h1>Welcome to Pizza House</h1>'

#Accept Order API
# @app.route('/order', methods="POST")
# def orderdetails():
#     # request_data = request.get_json()
#     args = {"order":["MediumPizza", "LargePizza"]}
#     le = background_order(args)
#     order = Order(order=args["order"]).save()
#     return jsonify(order)



    
@app.route('/order', methods="POST")
def OrderQueue():
    # args = request.get_json()
    args = {"order": ["Pizza50", "Pizza58"]}
    order = Order(order=args["order"]).save()
    job = q.enqueue(background_order, args)
    q_len = len(q)
    return f"Task ({job.id}) added to queue at({job.enqueued_at}). {q_len} task in queue"
    # return jsonify(order)


#Get Order Details API
@app.route('/getorders')
def getorders():
    li = []
    for order in Order.objects():
        li.append(order)
    return jsonify(li)

@app.route('/getorders/<orderid>')
def getordersbyid(orderid):
    if orderid not in Order.objects():
        abort(404, message="Order id doesn't exist")
    else:
        orderdetails = Order.objects.get(pk=orderid)
        return jsonify(orderdetails)



if __name__ == "__main__":
    app.run(debug=True)