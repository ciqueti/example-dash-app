# Plotly Dash Course - Session 2
# Callbacks -> Multiple Outputs and Multiple Inputs

from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_ag_grid as dag
import json

# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Plotly graphs
fig = px.histogram(df, x='continent', y='pop', histfunc='avg')

# Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.Div(children='My First App with Data, Graph, and Controls', id="html-div"),
    html.Hr(),
    dcc.Dropdown(options=["NYC", "MTL", "SF"], value="NYC", id="demo-dropdown"),
    dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'], value='lifeExp', id='column-options'),
    dag.AgGrid(
        id="grid",
        rowData=df.to_dict("records"),
        columnDefs=[{"field": i} for i in df.columns],
        dashGridOptions={"rowSelection" : "single"}
    ),
    dcc.Graph(figure=fig, id='graph1')
])

# Add controls to build the interaction
@callback(
    Output(component_id='graph1', component_property='figure'),
    Output(component_id="html-div", component_property="children"),

    Input(component_id='column-options', component_property='value'),
    Input(component_id="demo-dropdown" ,component_property="value"),
    Input(component_id="grid" , component_property="selectedRows")
)

def update_graph(radio_btn, dropdown_value, selected_row): # Each args function is gonna be from an Input callback, in the right order

    # print(selected_row[0]["country"])
    print(df[df["country"] == selected_row[0]["country"]])

    html_div = f"Drowpdown selected {dropdown_value}"

    fig = px.histogram(df, x='continent', y=radio_btn, histfunc='avg')

    return fig, html_div  # The return object will be placed/assigned in the Output property, in the right order


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
