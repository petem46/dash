from app import server
import flask
from flask import render_template

import dash
import dash_core_components as dcc
import dash_html_components as html

# server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server, url_base_pathname='/dashapp/')
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),
    html.Label(['', html.A('Home', href='/')]),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])



@server.route("/")
def index():
    return render_template("public/index.html")

@server.route("/about")
def about():
    return render_template("public/about.html")
