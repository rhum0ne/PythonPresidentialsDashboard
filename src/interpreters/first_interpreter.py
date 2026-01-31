import pandas as pd
from .base import Interpreter

class FirstInterpreter(Interpreter):
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
            self.getDepartmentLabelName(),
            "Code circonscription législative",
            "Libellé circonscription législative",
            "Inscrits",
            self.getAbstentionsColumnName(),
            "Votants",
            "Blancs",
            "Nuls",
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
                    self.getDepartmentLabelName(): "first",
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
    
    def getDepartmentLabelName(self) -> str:
        return "Libellé département"
    
    def getAbstentionsColumnName(self) -> str:
        return "Abstentions"
    
    def getDepartment4MainData(self, tour: int, department_code: str) -> dict[str, int]:
        df = self.getGlobalData(tour)
        df = df[df[self.getDepartmentCodeColumnName()] == department_code]
        inscrits = df["Inscrits"]
        votants = df["Votants"]
        blancs_nuls = df["Blancs"] + df["Nuls"]
        abstention = df[self.getAbstentionsColumnName()]
        
        return {
            "inscrits": int(inscrits),
            "votants": int(votants),
            "blancs_nuls": int(blancs_nuls),
            "abstention": int(abstention)
        }
    
    def get4MainData(self, tour: int) -> dict[str, int]:
        df = self.getGlobalData(tour)
        inscrits = df["Inscrits"].sum()
        votants = df["Votants"].sum()
        blancs_nuls = df["Blancs"].sum() + df["Nuls"].sum()
        abstention = df[self.getAbstentionsColumnName()].sum()
        
        return {
            "inscrits": int(inscrits),
            "votants": int(votants),
            "blancs_nuls": int(blancs_nuls),
            "abstention": int(abstention)
        }