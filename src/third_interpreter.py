import pandas as pd
from interpreter import Interpreter;

class ThirdInterpreter(Interpreter):
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
            f"data/{self.year}/{tour}/{self.file_name}"
        )

        df = pd.read_csv(path, sep=";")

        # Colonnes utiles
        colonnes_utiles = [
            self.getDepartmentCodeColumnName(),
            "département",
            "circonscription",
            "Inscrits",
            self.getAbstentionsColumnName(),
            "Votants",
            self.getAbstentionsColumnName(),
            self.getAbstentionsColumnName(),
        ]
        # Récupération des colonnes utiles
        df2024_t1_clean = df[colonnes_utiles].copy()

        # Normalisation des codes département
        df2024_t1_clean["Code département"] = (
            df2024_t1_clean["Code département"].astype(str).str.zfill(2)
        )

        # Agrégation par département
        df_dep = (
            df2024_t1_clean.groupby("Code département", as_index=False)
            .agg(
                {
                    "Inscrits": "sum",
                    "Votants": "sum",
                    "Abstentions": "sum",
                    "Blancs": "sum",
                    "Nuls": "sum",
                }
            )
            .reset_index(drop=True)
        )
    
        return df_dep
    
    def getDepartmentCodeColumnName(self) -> str:
        return "Code département"
    
    def getAbstentionsColumnName(self) -> str:
        return "Blancs et nuls"