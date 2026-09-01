import pandas as pd

title = '\n1. Carregue o dataset e chame describe(include="all"), identifique tipos e nulos.\n'

print(title)

df = pd.read_csv("../data/raw/heart_disease_uci.csv")

print(df.describe(include="all"))

print()

info_df = pd.DataFrame(
    {
        "Tipo de Dado": df.dtypes,
        "Valores Nulos": df.isnull().sum(),
        "Valores Não-Nulos": df.notnull().sum(),
    }
)
print(info_df)

print()
