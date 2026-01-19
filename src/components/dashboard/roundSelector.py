from dash import dcc

class RoundSelector:
    def __init__(self):
        self.available_rounds = [1, 2]
        self.selected_round = 1
        self.style = {'width': '45%'}

    def selectRound(self, round: int):
        if round in self.available_rounds:
            self.selected_round = round
            return True
        # else:
        #     raise ValueError(f"Year {year} is not available.")

    def getSelectedRound(self) -> int:
        return self.selected_round

    def getStyle(self) -> dict:
        return self.style
    
    def getDropdown(self) -> dcc.Dropdown:
        return dcc.Dropdown(
            id="round",
            options=[
                {"label": round, "value": round} for round in self.available_rounds],
            value=self.selected_round,
            clearable=False
        )