from dash import html
from src.utils.style import *

class MainDataPanel:
    def __init__(self):
        pass

    def getPanel(self):
        return html.Div(
            id="kpi-container",
            style={
                'display': 'grid',
                'gridTemplateColumns': 'repeat(2, 1fr)',
                'gridTemplateRows': 'repeat(2, 1fr)',
                'border-top': f'1px solid {SECONDARY_DARK}',
                'height': '80%',
            },
            children=[
                html.Div([
                    html.H4("Inscrits"),
                    html.H2(id="kpi-inscrits")
                ], style={"textAlign": "center"}),

                html.Div([
                    html.H4("Votants"),
                    html.H2(id="kpi-votants")
                ], style={"textAlign": "center"}),

                html.Div([
                    html.H4("Blancs / Nuls"),
                    html.H2(id="kpi-blancs-nuls")
                ], style={"textAlign": "center"}),

                html.Div([
                    html.H4("Abstentions"),
                    html.H2(id="kpi-abstention")
                ], style={"textAlign": "center"}),
            ]
        )