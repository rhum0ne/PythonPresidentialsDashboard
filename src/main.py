import pandas as pd
import dash
from dash import Dash, Input, Output, html, dcc
import plotly.express as px
import requests

df2024_t1 = pd.read_csv('data/2024/1/resultats-definitifs-par-circonscriptions-legislatives.csv', sep=';')

# colonnes_utiles = (
#     ['Code département', 'Libellé département', 
#      'Code circonscription législative', 'Libellé circonscription législative',
#      'Inscrits', 'Votants', 'Exprimés'] +
#     [col for col in df2024_t1.columns if 'Nuance candidat' in col] +
#     [col for col in df2024_t1.columns if 'Nom candidat' in col] +
#     [col for col in df2024_t1.columns if 'Prénom candidat' in col] +
#     [col for col in df2024_t1.columns if col.startswith('Voix ')] +
#     [col for col in df2024_t1.columns if '% Voix' in col] +
#     [col for col in df2024_t1.columns if 'Elu' in col]
# )
# Code du département | Libellé du département | Code de la circonscription | Libellé de la circonscription | Code de la commune | Libellé de la commune | Inscrits | Abstentions | Votants | Blancs | Nuls
colonnes_utiles = ["Code département", "Libellé département", "Code circonscription législative", "Libellé circonscription législative", "Inscrits", "Abstentions", "Votants", "Blancs", "Nuls"]

# récupération des colonnes utiles
df2024_t1_clean = df2024_t1[colonnes_utiles]

df2024_t1_clean["Code département"] = (
    df2024_t1_clean["Code département"]
    .astype(str)
    .str.zfill(2)
)

# Agrégation par département
df_dep = df2024_t1_clean.groupby("Code département").agg({
    "Inscrits": "sum",
    "Votants": "sum",
    "Abstentions": "sum",
    "Blancs": "sum",
    "Nuls": "sum"
}).reset_index()

print(df_dep)

# -------------------------------------------------------------------
# 2. Charger le geojson des départements
# -------------------------------------------------------------------
geojson_url = "https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/departements.geojson"
departements_geojson = requests.get(geojson_url).json()

# -------------------------------------------------------------------
# 3. App Dash
# -------------------------------------------------------------------
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Votes élections législatives - Carte de France"),
    
    dcc.Dropdown(
        id="variable",
        options=[
            {"label": "Inscrits", "value": "Inscrits"},
            {"label": "Votants", "value": "Votants"},
            {"label": "Abstentions", "value": "Abstentions"},
            {"label": "Blancs", "value": "Blancs"},
            {"label": "Nuls", "value": "Nuls"},
        ],
        value="Votants",
        clearable=False
    ),

    dcc.Graph(id="carte_france")
])

# -------------------------------------------------------------------
# 4. Callback de mise à jour
# -------------------------------------------------------------------
@app.callback(
    Output("carte_france", "figure"),
    Input("variable", "value")
)
def update_map(variable):
    fig = px.choropleth_mapbox(
        df_dep,
        geojson=departements_geojson,
        locations="Code département",
        featureidkey="properties.code",
        color=variable,
        mapbox_style="carto-positron",
        zoom=5,
        center={"lat": 46.5, "lon": 2.5},
        opacity=0.7,
        color_continuous_scale="Viridis"
    )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig

# -------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)