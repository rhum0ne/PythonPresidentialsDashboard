import pandas as pd
import dash
from dash import Dash, Input, Output, html, dcc
import plotly.express as px
import requests
from interpreter import Interpreter
from data import getData

def launchDashboard():
    print("Lancement du dashboard...")
    interpreter = getData(2024)
    df_dep = interpreter.getFirst() 

    print(df_dep)

    # -------------------------------------------------------------------
    # 2. Charger le geojson des départements
    # -------------------------------------------------------------------
    geojson_url = (
        "https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/"
        "departements.geojson"
    )
    departements_geojson = requests.get(geojson_url).json()

    # -------------------------------------------------------------------
    # 3. App Dash
    # -------------------------------------------------------------------
    app = dash.Dash(__name__)

    app.layout = html.Div(
        [
            html.H1("Votes élections législatives - Carte de France"),
            dcc.Dropdown(
                id="variable",
                options=[
                    {"label": "Inscrits", "value": "Inscrits"},
                    {"label": "Votants", "value": "Votants"},
                    {"label": "Abstentions", "value": "Abstentions"},
                    {"label": "Blancs", "value": "Blancs"},
                    {"label": "Nuls", "value": "Nuls"},
                ],
                value="Votants",
                clearable=False,
            ),
            dcc.Graph(id="carte_france"),
        ]
    )

    # -------------------------------------------------------------------
    # 4. Callback de mise à jour
    # -------------------------------------------------------------------
    @app.callback(
        Output("carte_france", "figure"),
        Input("variable", "value"),
    )
    def update_map(variable):
        fig = px.choropleth_mapbox(
            df_dep,
            geojson=departements_geojson,
            locations="Code département",
            featureidkey="properties.code",
            color=variable,
            mapbox_style="carto-positron",
            zoom=5,
            center={"lat": 46.5, "lon": 2.5},
            opacity=0.7,
            color_continuous_scale="Viridis",
        )
        fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
        return fig

    return app
