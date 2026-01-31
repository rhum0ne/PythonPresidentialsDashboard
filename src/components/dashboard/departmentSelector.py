from dash import dcc

class DepartmentSelector:
    def __init__(self, app):
        self.app = app
        self.selected_department = "01 - Ain"

    def get_content(self):
        return dcc.Dropdown(
            id="department_dropdown",
            options=[{'label': f'Department {i}', 'value': i} for i in range(1, 96)],
            value=self.selected_department,
            clearable=False,
        )