import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

title = '\n7. Bônus: correlacione Total e Rating com scatter plot.\n'

print(title)

df = pd.read_csv("../data/raw/vendas_1000_registros.csv")

corr = df[["Total", "Rating"]].corr()

plt.subplots(figsize=(8, 4))

sns.regplot(
    data = df,
    x = "Total",
    y = "Rating"
)

plt.title("Correlacao (Total x Avaliação)")
plt.xlabel("Total (R$)")
plt.ylabel("Avaliação")
plt.tight_layout()

# plt.show()
plt.savefig("../img/atividade_07.png", dpi=300)
print("Gráfico -> '../img/atividade_07.png'")

print()
