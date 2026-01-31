from dash import dcc

class VariableSelector:
    def __init__(self, id: str):
        self.id = id
    
    def get_dropdown(self) -> dcc.Dropdown:
        return dcc.Dropdown(
            id=self.id,
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