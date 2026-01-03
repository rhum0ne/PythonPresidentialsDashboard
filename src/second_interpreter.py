import pandas as pd
from interpreter import Interpreter;

class SecondInterpreter(Interpreter):
    def __init__(self, year: int, file_name: str = "data.xlsx"):
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

        df = pd.read_excel(path)

        # Colonnes utiles
        colonnes_utiles = [
            self.getDepartmentCodeColumnName(),
            "Libellé du département",
            "Code de la circonscription",
            "Libellé de la circonscription",
            "Inscrits",
            self.getAbstentionsColumnName(),
            "Votants",
            "Blancs",
            "Nuls",
        ]
        # Récupération des colonnes utiles
        df2024_t1_clean = df[colonnes_utiles].copy()

        # Normalisation des codes département
        df2024_t1_clean["Code du département"] = (
            df2024_t1_clean["Code du département"].astype(str).str.zfill(2)
        )

        # Agrégation par département
        df_dep = (
            df2024_t1_clean.groupby("Code du département", as_index=False)
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
        return "Code du département"
    
    def getAbstentionsColumnName(self) -> str:
        return "Abstentions"