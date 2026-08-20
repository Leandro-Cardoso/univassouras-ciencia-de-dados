import pandas as pd

title = '\n3. Calcule o total de vendas por filial (Branch) usando groupby.\n'

print(title)

df = pd.read_csv("../data/raw/vendas_1000_registros.csv")

print(df.groupby("Branch").agg({"Total": "sum"}))

print()
