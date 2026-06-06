import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output
df = pd.read_csv(
    r"C:\Users\mouood system\Downloads\superstore_final_dataset (1).csv\superstore_final_dataset (1).csv", encoding="latin1")

app = Dash(__name__)
app.layout = html.Div([
    html.H1("Sales Dashboard", style={"textAlign": "center"}),

    html.Label("Select Category:"),
    dcc.Dropdown(
        id="category-filter",
        options=[{"label": c, "value": c} for c in df["Category"].unique()],
        value=None,
        placeholder="All Categories"
    ),
    dcc.Graph(id="region-chart"),
    dcc.Graph(id="trend-chart")
])


@app.callback(
    Output("region-chart", "figure"),
    Output("trend-chart", "figure"),
    Input("category-filter", "value")
)
def update_charts(selected_category):
    filtered = df if not selected_category else df[df["Category"]
                                                   == selected_category]

    region_fig = px.bar(
        filtered.groupby("Region")[["Sales"]].sum().reset_index(),
        x="Region", y="Sales", title="Sales by Region"
    )

    filtered["Order_Date"] = pd.to_datetime(
        filtered["Order_Date"], dayfirst=True)
    trend = filtered.groupby(filtered["Order_Date"].dt.to_period("M"))[
        "Sales"].sum().reset_index()
    trend["Order_Date"] = trend["Order_Date"].astype(str)
    trend_fig = px.line(trend, x="Order_Date", y="Sales",
                        title="Monthly Sales Trend")

    return region_fig, trend_fig


if __name__ == "__main__":
    app.run(debug=True)
