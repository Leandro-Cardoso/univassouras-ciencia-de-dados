import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print('\n4. Faça um boxplot de thalach (frequência cardíaca máxima) por target (doença cardíaca).\n')

df = pd.read_csv("../data/raw/heart_disease_uci.csv")

sns.set_theme(style="whitegrid")

plt.figure(figsize=(8, 6))
sns.boxplot(x="target", y="thalach", data=df, palette="Set2")

plt.title(
    "Boxplot de Frequência Cardíaca Máxima (thalach) por Diagnóstico (target)"
)
plt.xlabel("Diagnóstico de Doença Cardíaca (0 = Não, 1 = Sim)")
plt.ylabel("Freq. Cardíaca Máxima (thalach)")

plt.savefig("../img/atividade_05.png", dpi=300)
print("Gráfico -> '../img/atividade_05.png'")

print()
