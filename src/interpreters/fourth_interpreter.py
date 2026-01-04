import pandas as pd
from .base import Interpreter

class FourthInterpreter(Interpreter):
    """
    Interpréteur pour les données de 1993.
    Les fichiers de 1993 n'ont pas de colonne "Blancs et nuls" mais ont "Votants" et "Exprimés".
    Cet interpréteur calcule "Blancs et nuls" = "Votants" - "Exprimés"
    """
    def __init__(self, year: int, file_name: str = "data.csv"):
        self._year = year
        self._file_name = file_name

    @property
    def year(self) -> int:
        return self._year

    @property
    def file_name(self) -> str:
        return self._file_name
    
    def getGlobalData(self, tour: int = 1) -> pd.DataFrame:
        path = (
            f"data/{self.year}/{tour}/cdsp_legi{self.year}t{tour}_circ.csv"
        )

        df = pd.read_csv(path, sep=",")

        # Calcul de la colonne "Blancs et nuls" à partir de Votants - Exprimés
        df["Blancs et nuls"] = df["Votants"] - df["Exprimés"]

        # Colonnes utiles
        colonnes_utiles = [
            self.getDepartmentCodeColumnName(),
            "département",
            "circonscription",
            "Inscrits",
            "Votants",
            self.getAbstentionsColumnName()
        ]
        
        # Récupération des colonnes utiles
        df_clean = df[colonnes_utiles].copy()

        # Normalisation des codes département
        df_clean["Code département"] = (
            df_clean["Code département"].astype(str).str.zfill(2)
        )

        # Agrégation par département
        df_dep = (
            df_clean.groupby("Code département", as_index=False)
            .agg(
                {
                    "Inscrits": "sum",
                    "Votants": "sum",
                    self.getAbstentionsColumnName(): "sum",
                }
            )
            .reset_index(drop=True)
        )
    
        return df_dep
    
    def getDepartmentCodeColumnName(self) -> str:
        return "Code département"
    
    def getAbstentionsColumnName(self) -> str:
        return "Blancs et nuls"
