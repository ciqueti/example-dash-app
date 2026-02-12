# Import packages
from dash import Dash, html

# Initialize the app -> Dash constructor
app = Dash()

# App Layout
app.layout = [html.Div(children="Hello World")]


# Run the App
if __name__ == "__main__":
    app.run(debug=True)