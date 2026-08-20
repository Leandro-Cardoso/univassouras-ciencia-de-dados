import pandas as pd

title = '\n2. Inspecione tipos de dados, dimensões e valores nulos.\n'

print(title)

df = pd.read_csv("../data/raw/vendas_1000_registros.csv")

print(df.info())

print()
