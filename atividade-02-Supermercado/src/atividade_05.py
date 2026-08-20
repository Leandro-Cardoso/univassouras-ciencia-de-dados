import pandas as pd
import matplotlib.pyplot as plt

title = '\n5. Crie um gráfico de barras comparando o faturamento por filial.\n'

print(title)

df = pd.read_csv("../data/raw/vendas_1000_registros.csv")

fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(
    df["Branch"],
    df["Total"],
    color="#3776ab"
)
ax.set_title("Faturamento por Filial")
ax.set_ylabel("Total (R$)")
ax.set_xlabel("Filial")
plt.tight_layout()

# plt.show()
plt.savefig("../img/atividade_05.png", dpi=300)
print("Gráfico -> '../img/atividade_05.png'")

print()
