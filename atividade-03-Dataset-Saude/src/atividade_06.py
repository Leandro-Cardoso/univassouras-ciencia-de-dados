import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print('\n6. Calcule a correlação de Pearson entre todas as variáveis numéricas e visualize com heatmap.\n')

df = pd.read_csv("../data/raw/heart_disease_uci.csv")

num_cols = ["age", "trestbps", "chol", "thalach", "oldpeak", "target"]
corr = df[num_cols].corr(method="pearson")
print(corr.round(2))

plt.figure(figsize=(8, 6))
sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    vmin=-1,
    vmax=1,
    linewidths=0.5,
)
plt.title("Matriz de Correlação de Pearson")

plt.savefig("../img/atividade_06.png", dpi=300)
print("\nGráfico -> '../img/atividade_06.png'")

print()
