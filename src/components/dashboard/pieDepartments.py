import plotly.express as px
from dash import Dash, dcc, html, Output, Input
from src.data import getData
import dash_bootstrap_components as dbc
from src.components.dashboard.departmentSelector import DepartmentSelector

class PieDepartments:
    def __init__(self, app: Dash):
        self.app = app
        self.departments_code: list = []
        self.departments_name: list = []
        self.selected_department: str = "01 - Ain"
        self.department_selector = DepartmentSelector(app)
        
        @app.callback(
            Output("department_dropdown", "options"),
            Output("department_dropdown", "value"),
            Input("year", "value"),
            Input("round", "value")
        )
        def update_departments_dropdown(year, round_value):
            interpreter = getData(year)
            df = interpreter.getGlobalData(round_value)
            codes = df[interpreter.getDepartmentCodeColumnName()].tolist()
            names = df[interpreter.getDepartmentLabelName()].tolist()
            self.update_data(codes, names)
            options = [f"{codes[i]} - {names[i]}" for i in range(len(codes))]
            return options, options[0]  # Set the first department as default values
        
        @app.callback(
            Output("pie_departements_graph", "figure"),
            Input("department_dropdown", "value"),
            Input("year", "value"),
            Input("round", "value")
        )
        def update_pie_graph(department_name, year, round_value):
            interpreter = getData(year)
            df = interpreter.getGlobalData(round_value)
            self.selected_department = department_name
            print("Department : ", self.selected_department)
            if self.selected_department.split(" - ")[1] in self.departments_name:
                index = self.departments_name.index(self.selected_department.split(" - ")[1])
                department_code = self.departments_code[index]
                department_name = self.departments_name[index]
                # data = df[df[interpreter.getDepartmentCodeColumnName()] == department_code].iloc[0]
                data = interpreter.getDepartment4MainData(round_value, department_code)
                
                inscrits = data["inscrits"]
                votants = data["votants"]
                blancs_nuls = data["blancs_nuls"]
                abstention = data["abstention"]

                per_votants = round((votants / inscrits) * 100, 2)
                per_blancs_nuls = round((blancs_nuls / inscrits) * 100, 2)
                per_abstention = round((abstention / inscrits) * 100, 2)
                
                labels = ['Votants', 'Abstention', 'Blancs et Nuls']
                values = [per_votants, per_abstention, per_blancs_nuls]
                fig = px.pie(
                    names=labels,
                    values=values,
                    title=f"Répartition pour le département {department_name} en {year} au tour {round_value}"
                )
                return fig

    def update_data(self, codes: list, names: list):
        self.departments_code = codes
        self.departments_name = names
        
    def get_content(self):
        return dbc.Col(
            [
                self.department_selector.get_content(),
                dcc.Graph(
                    id="pie_departements_graph",
                    config={
                        'displayModeBar': False,
                        'scrollZoom': False,
                    }
                )
            ],
            style={'display': 'flex', 'flex-direction': 'column', 'gap': '5px', 'width': '100%'}
        )