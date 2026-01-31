from dash import Dash, dcc, html, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px

class ComparePage:
    def __init__(self, app: Dash):
        self.app = app
    
        @app.callback(
            Output("compare_graph", "figure"),
        )
        def update_compare_graph():
            # Example static data for comparison
            fig = px.scatter(x=[1, 2, 3], y=[4, 5, 6], title="Compare Graph Example")
            return fig
    
    def get_content(self):
        return html.Div(
            [
                dbc.Row(
                    [
                        ]),
                dcc.Graph(
                    id="compare_graph",
                    figure=px.scatter(x=[1, 2, 3], y=[4, 5, 6], title="Compare Graph Example")
                )
            ]
        )