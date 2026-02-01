import pandas as pd
from dash import Dash, Input, Output, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import requests
from src.utils.style import *
from src.data import getData, getAvailableYears
from src.components.dashboard.tabsNavigator import TabsNavigator
from src.components.common.header import Header
from src.pages.HomePage import HomePage
from src.pages.ElectionPage import ElectionPage

def launchDashboard():
    print("Lancement du dashboard...")

    available_years = getAvailableYears()
    tabs_navigator = TabsNavigator()

    # -------------------------------------------------------------------
    # 2. Charger le geojson des départements
    # -------------------------------------------------------------------
    geojson_url = (
        "https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/"
        "departements.geojson"
    )
    departements_geojson = requests.get(geojson_url).json()

    # -------------------------------------------------------------------
    # 3. App Dash
    # -------------------------------------------------------------------
    app = Dash(
        __name__,
        external_stylesheets=[
            'https://use.fontawesome.com/releases/v6.0.0/css/all.css'
        ],
        suppress_callback_exceptions=True,
        # prevent_initial_callbacks='initial_duplicate'
    )
    
    # PAGES
    
    homePage = HomePage(app=app,departements_geojson=departements_geojson, available_years=available_years, tabs_navigator=tabs_navigator)
    election_page = ElectionPage(app, tabs_navigator)
    
    pages = [homePage, election_page]
    header = Header(app, tabs_navigator, available_years, pages)

    app.layout = dbc.Container(
        [
            dbc.Col(
                [
                    tabs_navigator.get_tabs_component()
                ],
                style={'width': 'max-content'}
            ),
            dbc.Col(
                [
                    header.get_content(),
                    html.Div(
                        tabs_navigator.get_content_container(),
                        style={'marginTop': '80px'}
                    )
                ],
                style={'width': 'calc(100vw - 60px)', 'overflow': 'auto', 'marginLeft': '60px'}
            )
        ],
        style={'display': 'flex', 'width': '100%'}
    )

    home_content = homePage.get_content()
    election_content = election_page.get_content()

    # -------------------------------------------------------------------
    # 4. Callback de mise à jour
    # -------------------------------------------------------------------
    
    # Changmeent d'onglet
    @app.callback(
        [Output("tab-content", "children")] + tabs_navigator.get_tab_style_outputs(),
        tabs_navigator.get_tab_inputs()
    )
    def update_tab_content(*clicks):
        from dash import callback_context
        
        if not callback_context.triggered:
            return [home_content] + tabs_navigator.get_all_tab_styles(0) # Par défaut on affiche home
        
        print("context : " + str(callback_context.triggered))
        
        button_id = callback_context.triggered[0]["prop_id"].split(".")[0]
        
        try:
            tab_index = int(button_id.split("-")[1])
        except (IndexError, ValueError):
            return [error_page("Onglet invalide.")] + tabs_navigator.get_all_tab_styles(0)
        
        contents = [
            home_content,       # 0
            election_content,   # 1
        ]
        
        if (0 <= tab_index < len(contents)):
            tabs_navigator.select_tab(tab_index)
            return [contents[tab_index]] + tabs_navigator.get_all_tab_styles(tab_index)
        
        return [error_page("Onglet non trouvé.")] + tabs_navigator.get_all_tab_styles(0)


    return app


def error_page(message: str) -> html.Div:
    return html.Div(
        [
            html.H1("Erreur"),
            html.P(message)
        ],
        style={'textAlign': 'center', 'marginTop': '50px'}
    )
