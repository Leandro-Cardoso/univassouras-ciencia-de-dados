import pandas as pd

print('\n2. Calcule média, mediana, desvio padrão e CV para age, trestbps e chol.\n')

df = pd.read_csv("../data/raw/heart_disease_uci.csv")

cols = ["age", "trestbps", "chol"]

resumo = pd.DataFrame(
    {
        "Média": df[cols].mean(),
        "Mediana": df[cols].median(),
        "Desvio Padrão": df[cols].std(),
        "CV (%)": (df[cols].std() / df[cols].mean()) * 100,
    }
)
print(resumo.round(2))

print()
