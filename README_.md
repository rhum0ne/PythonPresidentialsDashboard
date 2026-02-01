User guide

Afin de déployer le dashboard dans un environnement virtuel, suivre les étapes suivantes :
git clone https://github.com/rhum0ne/PythonPresidentialsDashboard.git projet
cd projet
python -m venv .venv
.venv/Scripts/activate.bat (ou double cliquer sur ce fichier depuis l'explorateur de fichiers)
pip install -m requirements.txt

Le projet est ensuite prêt à être lancé

Data

Les données utilisées sont des données officielles provenant de https://www.data.gouv.fr/pages/donnees-des-elections. Nous avons traité les données des élections législatives depuis l'année 1958 jusqu'à 2024

User Guide

L'architecture générale se décompose en 2 parties : - /data, répertorie les datasets - /src, regroupe tout le code et l'architecture métier du projet

Dans /src : - /components - /common, regroupe les composants communs aux pages - /dashboard, regroupe les composants utilisés pour créer les éléments du dashboard (graphiques, menus déroulants, ...) - /interpreters, regroupe les classes qui permettent de filtrer et traiter les données selon les années - /pages, les différentes pages du dashboard - /utils, des fichiers utilitaires comme des fonctions ou des constantes

Rapport d'analyse

Ce dashboard nous permet principalement de constater que la proportion de votants, d'abstentions et de votes blancs/nuls par rapport au nombre de personnes inscrites, sont très similaires par départements. Leur répartition suit plus ou moins de près la répartition globale de l'élection. Le taux de votes blancs/nuls étant rarement dupérieur à 5%, celui des abstention varie autour des 30%.

Copyright

Nous déclarons sur l'honneur que le code a été fourni par nous-mêùe.
