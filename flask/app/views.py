from app import app
import flask
from flask import render_template

import dash
import dash_core_components as dcc
import dash_html_components as html

@app.route("/")
def index():
    return render_template("public/index.html")

@app.route("/about")
def about():
    return render_template("public/about.html")
