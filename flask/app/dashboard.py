from app import app
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# external JavaScript files
external_scripts = [
    # 'https://www.google-analytics.com/analytics.js',
    # {'src': 'https://cdn.polyfill.io/v2/polyfill.min.js'},
    # {
    #     'src': 'https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.10/lodash.core.js',
    #     'integrity': 'sha256-Qqd/EfdABZUcAxjOkMi8eGEivtdTkh3b65xCZL4qAQA=',
    #     'crossorigin': 'anonymous'
    # },
    {
        'src': 'https://code.jquery.com/jquery-3.3.1.slim.min.js',
        'integrity': 'sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo',
        'crossorigin': 'anonymous'
    },
    {
        'src': 'https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js',
        'integrity': 'sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1',
        'crossorigin': 'anonymous'
    },
    {
        'src': 'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js',
        'integrity': 'sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM',
        'crossorigin': 'anonymous'
    }
]

# external CSS stylesheets
external_stylesheets = [
    # 'https://codepen.io/chriddyp/pen/bWLwgP.css',
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T',
        'crossorigin': 'anonymous'
    }
]

dashboard = dash.Dash(__name__,
            server=app, url_base_pathname='/dashapp/',
            external_scripts=external_scripts,
            external_stylesheets=external_stylesheets)

dashboard.layout = html.Div([
    html.H1('Hello From Dash In Flask in Docker through Nginx',className='bg-info text-center'),
    html.Div([
        html.Div('Dash: A web application framework for Python.'),
        html.Div(dcc.Input(id='input', value='Callback Text Demo', type='text')),
        html.Div(id='output'),
        html.Label(['', html.A('Home', href='/')])
    ],className="px-3 mx-5 mb-3 bg-white"),
    #dashboard row 1
    html.Div([
        #graph col-8 width
        html.Div([
            dcc.Graph(
                id='example-graph1-1',
                figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                        {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                    ],
                    'layout': {
                        'title': 'Chart 1-1 col-8',
                        'legend': {
                            'orientation': 'h',
                            'xanchor': 'center',
                            'x':'0.5',
                            'bordercolor': 'grey',
                            'borderwidth': '1',
                        },
                    }
                }
        )],className='col-8',id='graph_div1-1'),
        # graph col-4 width
        html.Div([
            dcc.Graph(
                id='example-graph1-2',
                figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                        {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                    ],
                    'layout': {
                        'title': 'Chart 1-2 col-4'
                    }
                }
        )],className='col-4',id='graph_div1-2')
    ],className="row px-5 mb-3"),
    # dashboard row 2
    html.Div([
        #graph col-4 width
        html.Div([
            dcc.Graph(
                id='example-graph2-1',
                figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                        {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                    ],
                    'layout': {
                        'title': 'Chart 2-1 col-4'
                    }
                }
        )],className='col-4',id='graph_div2-1'),
        # graph col-4 width
        html.Div([
            dcc.Graph(
                id='example-graph2-2',
                figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                        {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                    ],
                    'layout': {
                        'title': 'Chart 2-2 col-4'
                    }
                }
        )],className='col-4',id='graph_div2-2'),
        # graph col-4 width
        html.Div([
            dcc.Graph(
                id='example-graph2-3',
                figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                        {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                    ],
                    'layout': {
                        'title': 'Chart 2-3 col-4'
                    }
                }
        )],className='col-4',id='graph_div2-3')
    ],className="row px-5 mb-3"),
],style={'background-color1':'teal'},className='pb-5 bg-secondary')


@dashboard.callback(
    Output(component_id='output', component_property='children'),
    [Input(component_id='input', component_property='value')]
)
def update_value(input_data):
    return 'Input: "{}"'.format(input_data)