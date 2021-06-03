from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from flask_pymongo.wrappers import MongoClient
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/phone_app")

@app.route("/")
def index():
    

