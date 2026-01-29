from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
from components.dashboard.yearSelector import YearSelector
from components.dashboard.roundSelector import RoundSelector
from components.dashboard.mainDataPanel import MainDataPanel
from components.dashboard.franceGraph import FranceGraph
from components.dashboard.tabsNavigator import TabsNavigator
from components.dashboard.histogram import Histogram
import plotly.express as px
from data import *
from utils.style import *

class HomePage:
    def __init__(self, app: Dash, available_years: list, departements_geojson: dict, tabs_navigator: TabsNavigator):
        self.app = app
        self.tabs_navigator = tabs_navigator
        # self.available_years = available_years
        self.departements_geojson = departements_geojson
        
        self.france_graph = FranceGraph()
        self.main_data_panel = MainDataPanel()
        # self.histogtam = Histogram()
        
        # self.year_selector = YearSelector(available_years=available_years)
        # self.round_selector = RoundSelector()
        
        self.selected_year = None
        self.selected_round = None
        self.selected_variable = None
        
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
                geojson=self.departements_geojson,
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
        
        # callback pour la mise à jour des KPI
        @app.callback(
        Output("kpi-inscrits", "children"),
        Output("kpi-votants", "children"),
        Output("kpi-blancs-nuls", "children"),
        Output("kpi-abstention", "children"),
        Input("year", "value"),
        Input("round", "value")
        )
        def update_kpis(year, round):
            print("kpi year : ", year)
            print("kpi round : ", round)
            interpreter = getData(year)

            data = interpreter.get4MainData(round)

            inscrits = data["inscrits"]
            votants = data["votants"]
            blancs_nuls = data["blancs_nuls"]
            abstention = data["abstention"]

            return (
                f"{inscrits:,}".replace(",", " "),
                f"{votants:,}".replace(",", " "),
                f"{blancs_nuls:,}".replace(",", " "),
                f"{abstention:,}".replace(",", " ")
            )

    def get_content(self):

        home_content = html.Div(
                [
                    self.tabs_navigator.get_tab_description(0),
                    html.H1("Votes élections législatives - Carte de France"),
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    # self.france_graph.getDropdown(),
                                    self.france_graph.getGraph()
                                ], 
                                style=self.france_graph.getStyle()
                            ),
                            dbc.Col(
                                [
                                    html.Div(
                                        [
                                            dbc.Row(
                                                [
                                                    html.H2("Informations générales")
                                                ],
                                                style={'display': 'flex', 'justifyContent': 'center'}
                                            )
                                        ],
                                        style={'width': 'auto', 'height': '20%'}
                                    ),
                                    self.main_data_panel.getPanel()
                                ],
                                style={'width': '45%', 'height': '50vh', 'border': f'1px solid {PRIMARY_DARK}', 'border-radius': '10px', 'padding': '15px', 'display': 'flex', 'flexDirection': 'column', 'gap': '5px'}
                            )
                        ],
                        style={'display': 'flex', 'justifyContent': 'space-around', 'width': '100%'}
                    ),
                ]
            )
        
        return home_content
    
    