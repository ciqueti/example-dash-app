# Plotly Dash Course - Session 3
# Callbacks -> Multiple Outputs and Multiple Inputs + Using with attributes

from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_ag_grid as dag

# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Plotly graphs
fig = px.histogram(df, x='continent', y='pop', histfunc='avg')
fig_scatter = px.scatter(df, x="gdpPercap", y="lifeExp", range_x=[10000, 40000], color="country")
fig_scatter.update_traces(showlegend=False)
fig_scatter.update_layout(font_size = 20)


# Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.Div(children='My First App with Data, Graph, and Controls'),
    html.Hr(),
    dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'], value='lifeExp', id='column-options'),
    dag.AgGrid(
        id="grid",
        rowData=df.to_dict("records"),
        columnDefs=[{"field": i} for i in df.columns],
    ),
    dcc.Graph(figure=fig, id='graph1'),
    dcc.Graph(figure=fig_scatter, id="graph2", hoverData=None)
])

# Add controls to build the interaction
@callback(
    Output(component_id='graph1', component_property='figure'),
    Output(component_id="grid", component_property="rowData"),

    Input(component_id='column-options', component_property='value'),
    Input(component_id="graph2", component_property="hoverData")
)
def update_graph(col_chosen, hover_scatter_plot):

    # print(hover_scatter_plot)

    try:
        x_axis_data = hover_scatter_plot["points"][0]["x"]
        # print(x_axis_data)

        dff_scatter = df[df["gdpPercap"] == x_axis_data]
        
    except (TypeError, KeyError, IndexError):
        dff_scatter = df
    
    # print(dff_scatter)


    dff = df[df.country.isin(["Albania", "Romania", "Iran", "India", "Algeria", "Egypt", "Australia", "Canada"])]
    fig = px.histogram(dff, x='continent', y=col_chosen, histfunc='avg', pattern_shape="country", title="Histogram", labels={"country" : "Countries"})

    return fig, dff_scatter.to_dict("records")

# Try to add the pattern_shape attribute to the histogram so that each country receives its own shape
# Update legend in the histogram from "country" to "Countries"
# In the Scatter Map, update the range attribute to show between 10k -> 40k
# Add color for each "continent"
# Disable Legends in Scatter Plot with Figure Reference 
# Increase font-size of axis and titles axis with Figure Reference -> Layouts
# Dash -> DCC -> Graph -> Graph Properties. Let's use the clickData and hoverData attributes 

# Run the app
if __name__ == '__main__':
    app.run(debug=True)