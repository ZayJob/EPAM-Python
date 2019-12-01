from app import app
from pymongo import MongoClient
from flask import render_template, redirect, request
from typing import Dict, Any


@app.route("/")
def index():
    client = MongoClient("mongo", 27017)
    db = client["News_feeds"]
    collection = db["News"]

    req = request.args

    collection.insert({"args": parse_args_from_request(req)})

    return render_template('index.html')


def parse_args_from_request(req):
    dict_args = {
        "source": req.get('url'),
        "limit": req.get('limit'),
        "date": req.get('date'),
        "to_pdf": req.get('to_pdf')
    }
    return dict_args


def run():
    pass
