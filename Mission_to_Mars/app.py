from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_news")

@app.route("/")
def index():
    list_news = mongo.db.list_news.find_one()
    return render_template("index_mars.html", list_news=list_news)    

@app.route("/scrape")
def scraper():
    list_news = mongo.db.list_news
    list_data = scrape_mars.scrape()
    list_news.update({}, list_data, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)