"""
Main app file (initialization app)
"""
import pandas as pd
from dash import Dash, dcc, html

# prepare data for using in app
data = (
    pd.read_csv("avocado.csv")
    .query("type== 'conventional' and region == 'Albany'")
    .assign(Date=lambda data: pd.to_datetime(data["Date"], format="%Y-%m-%d"))
    .sort_values(by="Date")
)

# create instance of Dash (init app)
app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(
            children="Avocado Analitics",
            style={"fontSize": "48px", "color": "red"},
        ),
        html.P(
            children=(
                "Analyze the behavior of avocado prices and the number"
                " of avocados sold in the US between 2015 and 2018"
            ),
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Date"],
                        "y": data["AveragePrice"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Average Price of Avocados"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Date"],
                        "y": data["Total Volume"],
                        "type": "Lines",
                    },
                ],
                "layout": {"title": "Avocados Sold"},
            },
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
