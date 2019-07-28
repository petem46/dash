import dash
import dash_core_components as dcc
import dash_html_components as html
import flask
# import views
# import admin_views
server = flask.Flask(__name__)
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

@server.route('/')
def index():
    return '''
<html>
<div>
    <h1>Flask App</h1>
    <a class="nav-link" href="/dashapp">Dash</a>
</div>
</html>
'''

if __name__ == '__main__':
    server.run(debug=True)