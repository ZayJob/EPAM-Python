from app import app
from flask import render_template, request
from typing import Dict, Any
from data.app.application import Application


@app.route("/")
def index():

    application = Application(parse_args_from_request())
    application.run_app()

    return render_template('index.html')


@app.route("/news")
def news():

    return render_template('news.html')


def parse_args_from_request() -> Dict[str, Any]:
    dict_args = {
        "source": request.args.get('url'),
        "limit": int(request.args.get('limit')),
        "date": request.args.get('date'),
        "to_pdf": bool(request.args.get('to_pdf'))
    }
    return dict_args
