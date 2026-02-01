from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
from src.components.dashboard.tabsNavigator import TabsNavigator
from src.components.dashboard.histogram import Histogram
from src.components.dashboard.pieDepartments import PieDepartments
import plotly.express as px
from src.data import *
from src.utils.style import *

class ElectionPage:
    def __init__(self, app: Dash, tabs_navigator: TabsNavigator):
        self.app = app
        self.tabs_navigator = tabs_navigator
        
        self.histogram = Histogram()
        self.pie_departments = PieDepartments(app)
        
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
            print(interpreter.getGlobalData(round_value).head())
            print("variable before : ", variable)
            if(variable == "Abstentions"):
                variable = interpreter.getAbstentionsColumnName()
            if(variable == "Blancs"):
                variable = interpreter.getBlancsColumnName()
            if(variable == "Nuls"):
                variable = interpreter.getNulsColumnName()
            print("variable after :", variable)
            columns = [
                interpreter.getDepartmentCodeColumnName(),
                variable
            ]
            df_dep = interpreter.getGlobalData(round_value)[columns]
            
            self.selected_year = year
            self.selected_round = round_value
            self.selected_variable = variable
            # remove mode bar, disable zoom on histogram
            fig = px.bar(x=df_dep[interpreter.getDepartmentCodeColumnName()], y=df_dep[variable], labels={'x': 'Départements', 'y': str(variable)}, title=f'Histogramme des {variable} en {year} au tour {round_value}')
            return fig
        
        @app.callback(
            Output("pie", "figure"),
            Input("year", "value"),
            Input("round", "value")
        )
        def update_pie(year, round_value):
            interpreter = getData(year)

            data = interpreter.get4MainData(round_value)

            inscrits = data["inscrits"]
            votants = data["votants"]
            blancs_nuls = data["blancs_nuls"]
            abstention = data["abstention"]
            
            per_votants = round((votants / inscrits) * 100, 2)
            per_blancs_nuls = round((blancs_nuls / inscrits) * 100, 2)
            per_abstention = round((abstention / inscrits) * 100, 2)
            
            labels = ['Votants', 'Blancs et Nuls', 'Abstention']
            values = [per_votants, per_blancs_nuls, per_abstention]
            fig = px.pie(names=labels, values=values, title=f'Repartition des votants, blancs/nuls et abstention en {year} au tour {round_value}')
            return fig
            

    def get_content(self):
        election_content = html.Div(
            [
                self.tabs_navigator.get_tab_description(1),
                dbc.Row(
                    [
                        dcc.Graph(
                            id="histogram", 
                            config={
                                'displayModeBar': False,
                                "scrollZoom": False,
                            }
                        )
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dcc.Graph(
                                    id="pie",
                                    config={
                                        'displayModeBar': False,
                                        'scrollZoom': False,
                                    },
                                )
                            ],
                            style={'width': '50%'}
                        ),
                        dbc.Col(
                            [
                                self.pie_departments.get_content()
                            ],
                            style={'width': '50%'}
                        )
                    ],
                    style={'display': 'flex', 'gap': '20px', 'width': '100%'}
                )
            ]
        )
        
        return election_content
    
    