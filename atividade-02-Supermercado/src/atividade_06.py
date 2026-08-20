import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

title = '\n6. Plote a distribuição da avaliação (Rating) com histograma + KDE.\n'

print(title)

df = pd.read_csv("../data/raw/vendas_1000_registros.csv")

plt.subplots(figsize=(8, 4))

sns.histplot(
    data = df,
    x = "Rating",
    kde = True,
    bins = 10,
    color = "#2d9d78",
)

plt.title("Distribuição das Avaliações")
plt.xlabel("Avaliação")
plt.ylabel("Frequência")
plt.tight_layout()

# plt.show()
plt.savefig("../img/atividade_06.png", dpi=300)
print("Gráfico -> '../img/atividade_06.png'")

print()
