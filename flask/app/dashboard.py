from app import app
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

dashboard = dash.Dash(__name__, server=app, url_base_pathname='/dashapp/')
dashboard.layout = html.Div(children=[
    html.H1(children='Hello From Dash In Flask in DOCKER through Nginx'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    html.Div(dcc.Input(id='input', value='Text', type='text')),
    html.Div(id='output'),

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


@dashboard.callback(
    Output(component_id='output', component_property='children'),
    [Input(component_id='input', component_property='value')]
)
def update_value(input_data):
    return 'Input: "{}"'.format(input_data)