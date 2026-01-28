from typing import Callable as function
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
from components.dashboard.tabsNavigator import TabsNavigator
from components.dashboard.yearSelector import YearSelector
from components.dashboard.roundSelector import RoundSelector

class Header:
    def __init__(self, app: Dash, tabsNavigator: TabsNavigator, available_years: list):
        self.app = app
        self.tabsNavigator = tabsNavigator
        self.available_years = available_years
        self.year_selector = YearSelector(available_years=available_years)
        self.round_selector = RoundSelector()
        self.selected_year = None
        self.selected_round = None
    
        @app.callback(
            Output("carte_france", "figure"),
            Output("histogram", "figure"),
            [Input(self.year_selector.id, "value"),
            Input(self.round_selector.id, "value")]
        )
        def on_selection_change(year, round_value):
            current_tab = self.tabsNavigator.select_tab
            self.selected_year = year
            self.selected_round = round_value
            print(f"Selected year: {self.selected_year}, Selected round: {self.selected_round}")
            match(current_tab):
                case 0:
                    print("Updatin home page")
                    return
                case 1:
                    print("Updating election page")
                    return
                case _:
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
                )
            ],
            style={'display': 'flex', 'justifyContent': 'space-between', 'padding': '10px', 'box-shadow': '2px 4px 8px 0 rgba(0, 0, 0, 0.1)'}
        )