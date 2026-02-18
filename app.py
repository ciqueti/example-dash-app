# Plotly Dash Course - Session 4 - Part 1 - Layout
# Dash Bootstrap Components

# KeyWords SizeScreen Behavior -> xs, sm, md, lg, xl, xxl

from dash import Dash, html
import dash_bootstrap_components as dbc

app = Dash(
    external_stylesheets=[dbc.themes.CYBORG]
)

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(dbc.Alert("One of three columns"), width=4),
        dbc.Col(dbc.Alert("2nd of three columns"), width=4),
        dbc.Col(dbc.Alert("3rd of three columns"), width=4)
    ]),
    dbc.Row([
        dbc.Col(dbc.Alert("One of four columns"), width=6, lg=3, md=2),
        dbc.Col(dbc.Alert("2nd of four columns"), width=6, lg=3, md =2),
        dbc.Col(dbc.Alert("3rd of four columns"), width=6, lg=3, md=2),
        dbc.Col(dbc.Alert("4th of four columns"), width=6, lg=3, md=2)
    ])
])

if __name__ == "__main__":
    app.run(debug=True)