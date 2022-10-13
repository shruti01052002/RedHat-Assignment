from ast import arg
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

r = redis.Redis()
q = Queue(connection=r)

def create_task(task_type):
    time.sleep(int(task_type) * 10)
    return True

def background_order(n):
    delay = 2
    print(f"Order running, simulating a {delay} second delay")
    time.sleep(delay)
    print(len(n))
    print("Order completed")
    return len(n)