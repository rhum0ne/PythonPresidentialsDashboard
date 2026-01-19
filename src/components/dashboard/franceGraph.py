from dash import dcc

class FranceGraph:
    def __init__(self):
        self.style = {'width': "45%", 'height': '50vh'}

    def getStyle(self):
        return self.style
    
    def getDropdown(self):
        return dcc.Dropdown(
                    id="variable",
                    options=[
                        {"label": "Inscrits", "value": "Inscrits"},
                        {"label": "Votants", "value": "Votants"},
                        {"label": "Abstentions", "value": "Abstentions"},
                        {"label": "Blancs", "value": "Blancs"},
                        {"label": "Nuls", "value": "Nuls"},
                    ],
                    value="Votants",
                    clearable=False,
                )

    def getGraph(self):
        return dcc.Graph(id="carte_france", config={'scrollZoom': True})