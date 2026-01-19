from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
from components.dashboard.yearSelector import YearSelector
from components.dashboard.roundSelector import RoundSelector
from components.dashboard.mainDataPanel import MainDataPanel
from components.dashboard.franceGraph import FranceGraph
from components.dashboard.tabsNavigator import TabsNavigator
from utils.style import *

class HomePage:
    def __init__(self, app: Dash, available_years: list, tabs_navigator: TabsNavigator):
        self.app = app
        self.tabs_navigator = tabs_navigator
        self.available_years = available_years
        
        self.france_graph = FranceGraph()
        self.main_data_panel = MainDataPanel();
        
        self.year_selector = YearSelector(available_years=available_years)
        self.round_selector = RoundSelector()
        
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
                ]
            )
        
        return home_content
    
    