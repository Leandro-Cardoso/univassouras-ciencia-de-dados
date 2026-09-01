import pandas as pd

print('\n3. Compare média vs. mediana de chol, a distribuição é simétrica?\n')

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
