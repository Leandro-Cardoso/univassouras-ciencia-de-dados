import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

print(
    "\n8. Bônus: gere um pairplot e identifique o par com maior correlação.\n"
)

df = pd.read_csv("../data/raw/heart_disease_uci.csv")

num_cols = ["age", "trestbps", "chol", "thalach", "oldpeak"]

corr_matrix = df[num_cols].corr(method="pearson")
corr_values = corr_matrix.values.copy()
np.fill_diagonal(corr_values, 0)
corr_matrix_no_diag = pd.DataFrame(
    corr_values, index=corr_matrix.index, columns=corr_matrix.columns
)
var1, var2 = corr_matrix_no_diag.abs().unstack().idxmax()
maior_corr = corr_matrix.loc[var1, var2]

resumo = pd.DataFrame(
    {
        "Variável 1": [var1],
        "Variável 2": [var2],
        "Maior Correlação": [maior_corr],
    }
)

print("Par com maior correlação entre as variáveis numéricas:")
print(resumo.round(2))

sns.set_theme(style="whitegrid")
pairplot = sns.pairplot(df, vars=num_cols, hue="target", palette="Set1")
pairplot.fig.suptitle(
    "Pairplot das Variáveis Numéricas por Target", y=1.02
)

plt.savefig("../img/atividade_08.png", dpi=300)
print("\nGráfico -> '../img/atividade_08.png'")

print()
