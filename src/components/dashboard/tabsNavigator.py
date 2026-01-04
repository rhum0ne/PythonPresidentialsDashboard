import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output

class TabsNavigator:
    
    def __init__(self):
        self.labels = ["Home", "Election", "Compare", "By Time", "By Politics"]
        self.icons = [
            "fa-solid fa-house",
            "fa-solid fa-check-to-slot", 
            "fa-solid fa-scale-balanced",
            "fa-solid fa-chart-line",
            "fa-solid fa-palette"
        ]
        self.descriptions = [
            "Vue d'ensemble des données électorales par département",
            "Informations détaillées sur une année d'élection spécifique",
            "Comparaison entre différentes élections ou départements",
            "Evolution d'une variable au fil du temps",
            "Evolution d'une couleur politique à travers les élections"
        ]
        self.selected_tab = 0
        self.nb_tabs = len(self.labels)
    
    def get_tabs_component(self):
        tabs_content = []
        
        for i in range(self.nb_tabs):
            tab_button = html.Div(
                [
                    html.I(
                        className=self.icons[i],
                        style={
                            "fontSize": "20px"
                        }
                    )
                ],
                id=f"tab-{i}",
                className="tab-button",
                style={
                    "padding": "15px",
                    "textAlign": "center",
                    "cursor": "pointer",
                    "borderRadius": "8px",
                    "marginBottom": "10px",
                    "transition": "all 0.3s",
                    "backgroundColor": "#f8f9fa" if i != self.selected_tab else "#007bff",
                    "color": "#000" if i != self.selected_tab else "#fff",
                }
            )
            tabs_content.append(tab_button)
        
        return html.Div(
            tabs_content,
            style={
                "width": "60px",
                "padding": "15px 5px",
                "backgroundColor": "#ffffff",
                "boxShadow": "2px 0 5px rgba(0,0,0,0.1)",
                "height": "100vh",
                "position": "fixed",
                "left": 0,
                "top": 0,
                "zIndex": 1000
            }
        )
    
    def get_content_container(self):
        return html.Div(
            id="tab-content",
            style={
                "marginLeft": "80px",
                "padding": "20px"
            }
        )
    
    def get_tab_description(self, tab_index):
        if 0 <= tab_index < self.nb_tabs:
            return html.Div(
                [
                    html.H3(
                        self.labels[tab_index],
                        style={"marginBottom": "10px"}
                    ),
                    html.P(
                        self.descriptions[tab_index],
                        style={
                            "fontSize": "16px",
                            "color": "#666",
                            "marginBottom": "30px"
                        }
                    )
                ]
            )
        return html.Div()
    
    def select_tab(self, tab_index):
        if 0 <= tab_index < self.nb_tabs:
            self.selected_tab = tab_index

        print(f"Selected tab: {self.selected_tab}")
    
    def get_tab_inputs(self):
        return [Input(f"tab-{i}", "n_clicks") for i in range(self.nb_tabs)]
    
    def get_tab_style_outputs(self):
        return [Output(f"tab-{i}", "style") for i in range(self.nb_tabs)]
    
    def get_tab_style(self, tab_index, is_selected):
        return {
            "padding": "15px",
            "textAlign": "center",
            "cursor": "pointer",
            "borderRadius": "8px",
            "marginBottom": "10px",
            "transition": "all 0.3s",
            "backgroundColor": "#007bff" if is_selected else "#f8f9fa",
            "color": "#fff" if is_selected else "#000",
        }
    
    def get_all_tab_styles(self, selected_index):
        return [self.get_tab_style(i, i == selected_index) for i in range(self.nb_tabs)]
