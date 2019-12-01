from app import app
from pymongo import MongoClient
from flask import render_template

#client = MongoClient("mongo", 27017)
#db = client["lol"]
#collection = db["kek"]
#collection.insert_one({"lol": "kek"})


@app.route("/")
def index():
    return render_template('index.html')
