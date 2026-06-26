import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Read data
df = pd.read_csv("formatted_sales_data.csv")

df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

app = Dash(__name__)

# Layout
app.layout = html.Div(

    style={
        "backgroundColor": "#F4F6F9",
        "padding": "30px",
        "fontFamily": "Arial"
    },

    children=[

        html.H1(
            "Soul Foods Pink Morsel Sales Dashboard",
            style={
                "textAlign": "center",
                "color": "#003366"
            }
        ),

        html.H3(
            "Select Region",
            style={"color": "#444"}
        ),

        dcc.RadioItems(
            id="region-selector",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "South", "value": "south"},
                {"label": "East", "value": "east"},
                {"label": "West", "value": "west"},
            ],
            value="all",
            inline=True,
            style={"marginBottom": "20px"}
        ),

        dcc.Graph(id="sales-graph")
    ]
)

# Callback
@app.callback(
    Output("sales-graph", "figure"),
    Input("region-selector", "value")
)
def update_graph(selected_region):

    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["Region"] == selected_region]

    fig = px.line(
        filtered_df,
        x="Date",
        y="Sales",
        color="Region",
        title="Pink Morsel Sales Over Time"
    )

    fig.update_layout(
        template="plotly_white",
        paper_bgcolor="#F4F6F9",
        plot_bgcolor="#FFFFFF",
        xaxis_title="Date",
        yaxis_title="Sales",
        title_x=0.5
    )

    return fig

# Run app
if __name__ == "__main__":
    app.run(debug=True)