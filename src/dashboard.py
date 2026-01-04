import pandas as pd
from dash import Dash, Input, Output, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import requests
from data import getData, getAvailableYears
from components.dashboard.franceGraph import FranceGraph
from components.dashboard.yearSelector import YearSelector
from components.dashboard.roundSelector import RoundSelector

def launchDashboard():
    print("Lancement du dashboard...")

    france_graph = FranceGraph()
    available_years = getAvailableYears()
    year_selector = YearSelector(available_years=available_years)
    round_selector = RoundSelector()

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
    app = Dash(__name__)

    app.layout = html.Div(
        [
            html.H1("Votes élections législatives - Carte de France"),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            france_graph.getDropdown(),
                            france_graph.getGraph()
                        ], 
                        style=france_graph.getStyle()
                    ),
                    dbc.Col(
                        [
                            html.P("Année :"),
                            year_selector.getDropdown(),
                            html.P("Tour :"),
                            round_selector.getDropdown(),
                            html.Div(id="invisible_debug_year", style={'display': 'none'}),
                            html.Div(id="invisible_debug_round", style={'display': 'none'}),
                        ],
                        style=year_selector.getStyle()
                    )
                ],
                style={'display': 'flex', 'justifyContent': 'space-around'}
            ),
        ]
    )

    # -------------------------------------------------------------------
    # 4. Callback de mise à jour
    # -------------------------------------------------------------------
    @app.callback(
        Output("carte_france", "figure"),
        [Input("variable", "value"),
         Input("year", "value"),
         Input("round", "value")]
    )
    def update_map(variable, year, round_value):
        print("update_map called")
        print("variable changed : ", variable)
        print("year : ", year)
        print("round : ", round_value)
        
        # Récupérer les données pour l'année et le tour sélectionnés
        interpreter = getData(year)
        df_dep = interpreter.getGlobalData(round_value)
        
        if(variable == "Abstentions"):
            variable = interpreter.getAbstentionsColumnName()
            
        fig = px.choropleth_mapbox(
            df_dep,
            geojson=departements_geojson,
            locations=interpreter.getDepartmentCodeColumnName(),
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

    @app.callback(
        Output("invisible_debug_year", "children"),
        Input("year", "value"),
    )
    def update_year(variable):
        year_selector.selectYear(variable)
        print("year changed : ", year_selector.getSelectedYear())
        return ""

    @app.callback(
        Output("invisible_debug_round", "children"),
        Input("round", "value"),
    )
    def update_round(variable):
        round_selector.selectRound(variable)
        print("round changed : ", round_selector.getSelectedRound())
        return ""

    return app
