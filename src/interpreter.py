import pandas as pd

class Interpreter:
    def getFirst(self):
        df2024_t1 = pd.read_csv(
            "data/2024/1/resultats-definitifs-par-circonscriptions-legislatives.csv",
            sep=";",
        )

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
        df2024_t1_clean = df2024_t1[colonnes_utiles].copy()

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