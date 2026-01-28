from dash import dcc

class FranceGraph:
    def __init__(self):
        self.style = {'width': "45%", 'height': '50vh'}

    def getStyle(self):
        return self.style

    def getGraph(self):
        return dcc.Graph(id="carte_france", config={'scrollZoom': True, 'displayModeBar': False})