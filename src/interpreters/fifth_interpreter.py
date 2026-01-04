import pandas as pd
from .base import Interpreter

class FifthInterpreter(Interpreter):
    """
    Interpréteur pour les données de 1986.
    Election législative à un seul tour avec scrutin proportionnel.
    Le fichier se trouve directement dans data/1986/ (pas de sous-dossiers 1/ ou 2/).
    """
    def __init__(self, year: int, file_name: str = "cdsp_legi1986_circ.csv"):
        self._year = year
        self._file_name = file_name

    @property
    def year(self) -> int:
        return self._year

    @property
    def file_name(self) -> str:
        return self._file_name
    
    def getGlobalData(self, tour: int = 1) -> pd.DataFrame:
        # Pour 1986, le fichier est directement dans data/1986/
        path = f"data/{self.year}/{self.file_name}"

        df = pd.read_csv(path, sep=",")

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
        df_clean["code département"] = (
            df_clean["code département"].astype(str).str.zfill(2)
        )

        # Agrégation par département
        df_dep = (
            df_clean.groupby("code département", as_index=False)
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
        return "code département"
    
    def getAbstentionsColumnName(self) -> str:
        return "Blancs et nuls"
