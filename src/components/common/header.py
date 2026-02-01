from typing import Callable as function
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
from src.components.dashboard.tabsNavigator import TabsNavigator
from src.components.dashboard.yearSelector import YearSelector
from src.components.dashboard.roundSelector import RoundSelector
from src.components.dashboard.variableSelector import VariableSelector

class Header:
    def __init__(self, app: Dash, tabsNavigator: TabsNavigator, available_years: list, pages: list):
        self.app = app
        self.tabsNavigator = tabsNavigator
        self.available_years = available_years
        self.year_selector = YearSelector(available_years=available_years, id="year")
        self.round_selector = RoundSelector(id="round")
        self.variable_selector = VariableSelector(id="variable")
        self.selected_year = None
        self.selected_round = None
        self.pages = pages
    
        @app.callback(
            Output("invisible_debug_year", "children"),
            [Input(self.year_selector.id, "value"),
            Input(self.round_selector.id, "value")],
        )
        def on_selection_change(year, round_value):
            self.selected_year = year
            self.selected_round = round_value
            return
            
    
    def get_content(self):
        return dbc.Row(
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
                ),
                dbc.Col(
                    [
                        html.P("Variable :", style={'margin-block': '0px', 'padding': '0px'}),
                        self.variable_selector.get_dropdown(),
                        html.Div(id="invisible_debug_variable", style={'display': 'none'}),
                    ],
                    style={'width': '45%', 'display': 'flex', 'flex-direction': 'column', 'gap': '5px'}
                )
            ],
            style={'display': 'flex', 'gap': '10px', 'justifyContent': 'space-between', 'padding': '10px', 'box-shadow': '2px 4px 8px 0 rgba(0, 0, 0, 0.1)', 'position': 'fixed', 'width': 'calc(100% - 90px)', 'z-index': '999', 'background-color': 'white'}
        )