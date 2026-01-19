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
        self.available_years = available_years
        self.departements_geojson = departements_geojson
        
        self.france_graph = FranceGraph()
        self.main_data_panel = MainDataPanel()
        self.histogtam = Histogram()
        
        self.year_selector = YearSelector(available_years=available_years)
        self.round_selector = RoundSelector()
        
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
            
            self.histogtam.update_data(df_dep)
            
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
        
        # callback pour la mise à jour de l'histogramme
        @app.callback(
        Output("histogram", "figure"),
        [Input("variable", "value"),
         Input("year", "value"),
         Input("round", "value")]
        )
        def update_histogram(variable, year, round_value):
            print("update histogram")
            interpreter = getData(year)
            columns = [
                interpreter.getDepartmentCodeColumnName(),
                variable
            ]
            df_dep = interpreter.getGlobalData(round_value)[columns]
            
            if(variable == "Abstentions"):
                variable = interpreter.getAbstentionsColumnName()
            
            self.selected_year = year
            self.selected_round = round_value
            self.selected_variable = variable
            fig = px.histogram(x=df_dep[interpreter.getDepartmentCodeColumnName()], y=df_dep[variable], labels={'x': 'Départements', 'y': ""+variable}, title=f'Histogramme des {variable} en {year} au tour {round_value}')
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
            # main_data_panel.setInterpreter(interpreter) # Mettre à jour l'interprète dans le panneau des données principales

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
        
        @app.callback(
        Output("invisible_debug_year", "children"),
        Input("year", "value"),
        )
        def update_year(variable):
            self.year_selector.selectYear(variable)
            print("year changed : ", self.year_selector.getSelectedYear())
            return ""

        @app.callback(
            Output("invisible_debug_round", "children"),
            Input("round", "value"),
        )
        def update_round(variable):
            self.round_selector.selectRound(variable)
            print("round changed : ", self.round_selector.getSelectedRound())
            return ""

    def get_content(self):

        home_content = html.Div(
                [
                    self.tabs_navigator.get_tab_description(0),
                    html.H1("Votes élections législatives - Carte de France"),
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    self.france_graph.getDropdown(),
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
                                                    dbc.Col(
                                                        [
                                                            html.P("Année :", style={'margin-block': '0px', 'padding': '0px'}),
                                                            self.year_selector.getDropdown(),
                                                            html.Div(id="invisible_debug_year", style={'display': 'none'}),
                                                        ],
                                                        style={'width': '45%', 'display': 'flex', 'flex-direction': 'column', 'gap': '5px'}
                                                    ),
                                                    dbc.Col(
                                                        [
                                                            html.P("Tour :", style={'margin-block': '0px', 'padding': '0px'}),
                                                            self.round_selector.getDropdown(),
                                                            html.Div(id="invisible_debug_round", style={'display': 'none'}),
                                                        ],
                                                        style={'width': '45%', 'display': 'flex', 'flex-direction': 'column', 'gap': '5px'}
                                                    )
                                                ],
                                                style={'display': 'flex', 'justifyContent': 'space-between'}
                                            )
                                        ],
                                        style={'width': 'auto', 'height': '20%'}
                                    ),
                                    self.main_data_panel.getPanel()
                                ],
                                style={'width': '45%', 'height': '50vh', 'border': f'1px solid {PRIMARY_DARK}', 'border-radius': '10px', 'padding': '15px', 'display': 'flex', 'flexDirection': 'column', 'gap': '5px'}
                            )
                        ],
                        style={'display': 'flex', 'justifyContent': 'space-around'}
                    ),
                    dcc.Graph(id="histogram", )
                ]
            )
        
        return home_content
    
    