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

class ElectionPage:
    def __init__(self, app: Dash, tabs_navigator: TabsNavigator):
        self.app = app
        self.tabs_navigator = tabs_navigator
        
        self.histogram = Histogram()
        
        self.selected_year = None
        self.selected_round = None
        self.selected_variable = None
        
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
            # remove mode bar, disable zoom on histogram
            fig = px.bar(x=df_dep[interpreter.getDepartmentCodeColumnName()], y=df_dep[variable], labels={'x': 'Départements', 'y': str(variable)}, title=f'Histogramme des {variable} en {year} au tour {round_value}')
            return fig

    def get_content(self):
        election_content = html.Div(
                [
                    dcc.Graph(
                        id="histogram", 
                        config={
                            'displayModeBar': False, 
                            "scrollZoom": False,
                            "doubleClick": False,
                            "displaylogo": False
                        }
                )
                ]
            )
        
        return election_content
    
    