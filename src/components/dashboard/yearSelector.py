from dash import dcc

class YearSelector:
    def __init__(self, available_years: list):
        self.available_years = sorted(available_years)
        self.selected_year = self.available_years[len(self.available_years) - 1] if self.available_years else None
        self.style = {'width': '45%'}

    def selectYear(self, year: int):
        if year in self.available_years:
            self.selected_year = year
            return True
        # else:
        #     raise ValueError(f"Year {year} is not available.")

    def getSelectedYear(self):
        return self.selected_year

    def getAvailableYears(self):
        return self.available_years
    
    def getStyle(self):
        return self.style
    
    def getDropdown(self):
        return dcc.Dropdown(
            id="year",
            options=[
                {"label": year, "value": year} for year in self.available_years],
            value=self.selected_year,
            clearable=False
        )