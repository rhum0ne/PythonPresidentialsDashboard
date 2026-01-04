"""
Module contenant tous les interpréteurs de données électorales.

Chaque interpréteur est adapté à un format de fichier spécifique et permet
de normaliser les données pour une utilisation cohérente dans l'application.

Interpréteurs disponibles:
- FirstInterpreter: Pour les données de 2024 (format CSV avec séparateur ;)
- SecondInterpreter: Pour les données de 2022 (format Excel)
- ThirdInterpreter: Pour les données de 2007, 2002, 1997, 1988 (format CSV avec colonne "Blancs et nuls")
- FourthInterpreter: Pour les données de 1993 (calcule "Blancs et nuls" à partir de Votants - Exprimés)
"""

from .base import Interpreter
from .first_interpreter import FirstInterpreter
from .second_interpreter import SecondInterpreter
from .third_interpreter import ThirdInterpreter
from .fourth_interpreter import FourthInterpreter

__all__ = [
    'Interpreter',
    'FirstInterpreter',
    'SecondInterpreter',
    'ThirdInterpreter',
    'FourthInterpreter'
]
