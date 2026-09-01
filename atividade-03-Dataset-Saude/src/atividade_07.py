import pandas as pd
import numpy as np

print('\n7. Teste com qui-quadrado se sex está associado a target.\n')

df = pd.read_csv("../data/raw/heart_disease_uci.csv")

observado = pd.crosstab(df["sex"], df["target"])
totais_linhas = observado.sum(axis=1).values
totais_colunas = observado.sum(axis=0).values
total_geral = len(df)
esperado = np.outer(totais_linhas, totais_colunas) / total_geral
chi2_stat = np.sum((observado.values - esperado) ** 2 / esperado)
dof = (observado.shape[0] - 1) * (observado.shape[1] - 1)

resumo = pd.DataFrame(
    {
        "Chi2": [chi2_stat],
        "Graus de Liberdade": [dof],
        "Total de Observações": [total_geral],
    }
)

print("Tabela de Contingência (sex vs target):")
print(observado)

print("\nFrequências Esperadas:")
print(pd.DataFrame(esperado, index=observado.index, columns=observado.columns).round(2))

print("\nResultado do Teste Qui-Quadrado:")
print(resumo.round(2))

print()
