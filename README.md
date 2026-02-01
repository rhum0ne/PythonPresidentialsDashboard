# 📊 Dashboard -- Élections législatives françaises

Ce projet propose un **dashboard interactif** permettant d'explorer les
résultats des élections législatives françaises selon différentes
années et tours.

---

## Installation du projet

Nous recommandons l'utilisation d'un **environnement virtuel**.
Dépo git du projet : https://github.com/rhum0ne/PythonPresidentialsDashboard.git

### 1️. Cloner le projet et se placer dans le dossier

```bash
cd chemin/vers/le/projet
```

### 2️. Créer un environnement virtuel

```bash
python -m venv .venv
```

### 3️. Activer l'environnement virtuel

**Windows :**

```bash
.venv\Scripts\activate
```

### 4 Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## 5 Lancer le dashboard

```bash
python main.py
```

Puis ouvrir l'adresse indiquée dans le terminal

---

## Données

Les données utilisées sont des **données officielles** provenant de :\
👉 https://www.data.gouv.fr/pages/donnees-des-elections

Le projet couvre les élections législatives de **1958 à 2024**.

---

## Architecture du projet

Le projet est structuré en deux parties principales :

    /data   → jeux de données
    /src    → code source du projet

### Contenu du dossier `/src`

---

Dossier Rôle

---

`/components` Composants génériques
réutilisables

`/common` Éléments partagés entre les
pages

`/dashboard` Composants spécifiques au
dashboard (graphiques,
menus, etc.)

`/interpreters` Classes de traitement et
filtrage des données selon
les années

`/pages` Pages du dashboard

`/utils` Fonctions utilitaires et
constantes

---

---

## Objectif d'analyse

Ce dashboard permet d'observer que :

- Les proportions de **votants**, **abstentions** et **votes
  blancs/nuls** par département suivent généralement la tendance
  nationale.
- Le taux de votes **blancs/nuls** dépasse rarement **5%**.
- Le taux d'**abstention** se situe fréquemment autour de **30%**.
- Les répartitions territoriales sont relativement homogènes à
  l'échelle nationale.

---

## Fonctionnalités principales

• Sélection de l'année et du tour\
• Carte de France par départements interactive\
• Indicateurs clés globaux par éléction\
• Visualisations par département

---

## © Auteurs

Romain ELETUFE et Anthony PRADIER,

Nous déclarons sur l'honneur que le code a été développé par nous-même.

---

## Technologies utilisées

- Python
- Dash
- Plotly
- Pandas
- numpy
