import pandas as pd
from interpreter import Interpreter;

class FirstInterpreter(Interpreter):
    def __init__(self, year: int):
        self._year = year

    @property
    def year(self) -> int:
        return self._year

    def getFirst(self, tour: int = 1) -> pd.DataFrame:
        path = (
            f"data/{self.year}/{tour}/"
            "resultats-definitifs-par-circonscriptions-legislatives.csv"
        )

        df = pd.read_csv(path, sep=";")

        # Colonnes utiles
        colonnes_utiles = [
            "Code département",
            "Libellé département",
            "Code circonscription législative",
            "Libellé circonscription législative",
            "Inscrits",
            "Abstentions",
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