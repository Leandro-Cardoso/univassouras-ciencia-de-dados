import pandas as pd
import numpy as np

print('\n4. Detecte outliers em chol usando IQR e Z-score, quantos encontrou?\n')

df = pd.read_csv("../data/raw/heart_disease_uci.csv")

cols = ["chol"]

q1 = df[cols].quantile(0.25)
q3 = df[cols].quantile(0.75)
iqr = q3 - q1
lim_inf_iqr = q1 - 1.5 * iqr
lim_sup_iqr = q3 + 1.5 * iqr

mean = df[cols].mean()
std = df[cols].std()
z_scores = (df[cols] - mean) / std

resumo = pd.DataFrame(
    {
        "Q1": q1,
        "Q3": q3,
        "IQR": iqr,
        "Lim Inf IQR": lim_inf_iqr,
        "Lim Sup IQR": lim_sup_iqr,
        "Outliers IQR": ((df[cols] < lim_inf_iqr) | (df[cols] > lim_sup_iqr)).sum(),
        "Média": mean,
        "Desvio Padrão": std,
        "Outliers Z-Score": (np.abs(z_scores) > 3).sum(),
    }
)
print(resumo.round(2))

print()
