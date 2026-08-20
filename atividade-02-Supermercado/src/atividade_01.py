import pandas as pd

title = '\n1. Carregue o arquivo supermarket_sales.csv com Pandas e exiba as 5 primeiras linhas.\n'

print(title)

df = pd.read_csv("../data/raw/vendas_1000_registros.csv")

print(df.head())

print()
