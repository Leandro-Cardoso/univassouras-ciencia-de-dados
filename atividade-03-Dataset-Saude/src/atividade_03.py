import pandas as pd

title = '\n3. Compare média vs. mediana de chol, a distribuição é simétrica?\n'

print(title)

df = pd.read_csv("../data/raw/heart_disease_uci.csv")

cols = ["chol"]

resumo = pd.DataFrame(
    {
        "Média": df[cols].mean(),
        "Mediana": df[cols].median(),
        "Assimetria": df[cols].skew(),
    }
)
print(resumo.round(2))

print()
