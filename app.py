# Plotly Dash Course - Session 4 - Setup
# Dash Bootstrap Components

from dash import Dash, html
import dash_bootstrap_components as dbc

app = Dash(
    external_stylesheets=[dbc.themes.CYBORG]
)

app.layout = dbc.Container([
    html.H1("Dash Bootstrap Alerts"),
    dbc.Alert("Hello, Bootstrap!", className="m-5", is_open=True, duration=4000)
])

if __name__ == "__main__":
    app.run()