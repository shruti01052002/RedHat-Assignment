from flask import Flask, render_template, request, redirect, url_for
# from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# from flask_mail import Mail
from flask_pymongo import PyMongo
import json
import os
main = Flask(__name__)
main.config['MONGO_URI'] = 'mongodb+srv://Shruti:2019b121002@pizza-house.sxrdcrv.mongodb.net/test'
pizza_house = PyMongo(main)


@main.route('/welcome')
def base():
    return '<h1>Welcome to Pizza House</h1>'


if __name__ == "__main__":
    main.run(debug=True)