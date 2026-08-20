import pandas as pd

title = '\n4. Identifique a linha de produto com maior ticket médio.\n'

print(title)

df = pd.read_csv("../data/raw/vendas_1000_registros.csv")

print(df.nlargest(1, 'Total'))

print()
