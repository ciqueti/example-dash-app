# Plotly Dash Course - Session 4 - Part 2 -> State
# State Callbacks -> Let's assume we want multiples components to be selected (dropdown, radio-button, date-picker) before updating the graph (activate the callback)

from dash import Dash, html, dcc, callback, Input, Output, State, no_update
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Initialize the app
app = Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])

# App layout
app.layout = dbc.Container([
    html.H1(children='Country Analysis'),
    html.Hr(),
    
    dbc.Row([
        dbc.Col([
            dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'], value='lifeExp', id='yaxis-options'),   
        ], width=6),
        dbc.Col([
            dcc.Dropdown(options=['country', 'continent'], value='continent', id='xaxis-options'),    
        ], width=6)
    ], className='mb-3'),

    dbc.Button("Submit", id="my-button", n_clicks=0),

    dbc.Row([
        dbc.Col([
            dcc.Graph(figure={}, id='graph1')
        ], width=12)
    ]),
])

# Add controls to build the interaction
@callback(
    Output(component_id='graph1', component_property='figure'),
    Input(component_id="my-button", component_property="n_clicks"),
    State(component_id='yaxis-options', component_property='value'),
    State(component_id='xaxis-options', component_property='value'),
    
)
def update_graph(_, y_chosen, x_chosen):
    fig = px.histogram(df, x=x_chosen, y=y_chosen, histfunc='avg')
    return fig


# Run the app
if __name__ == '__main__':
    app.run(debug=True)