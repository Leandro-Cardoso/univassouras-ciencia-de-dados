# Exercício Prático

Cenário: Dataset de Saúde (Heart Disease)

Dataset com 303 pacientes e 14 variáveis clínicas. Use Python + Pandas + Scipy + Seaborn para fazer uma análise descritiva completa.

## Colunas do Dataset

| Variável | Descrição | Tipo |
| --- | --- | --- |
| age | Idade em anos | int |
| sex | Sexo (0=F, 1=M) | cat |
| trestbps | Pressão arterial em repouso | int |
| chol | Colesterol sérico (mg/dl) | int |
| thalach | Freq. cardíaca máxima | int |
| oldpeak | Depressão ST pelo exercício | float |
| target | Doença cardíaca (0=não, 1=sim) | cat |

## Atividades

1. [Carregue o dataset e chame describe(include="all"), identifique tipos e nulos.](https://github.com/Leandro-Cardoso/univassouras-ciencia-de-dados/blob/main/atividade-03-Dataset-Saude/src/atividade_01.py)

2. [Calcule média, mediana, desvio padrão e CV para age, trestbps e chol.](https://github.com/Leandro-Cardoso/univassouras-ciencia-de-dados/blob/main/atividade-03-Dataset-Saude/src/atividade_02.py)

3. [Compare média vs. mediana de chol, a distribuição é simétrica?](https://github.com/Leandro-Cardoso/univassouras-ciencia-de-dados/blob/main/atividade-03-Dataset-Saude/src/atividade_03.py)

4. [Detecte outliers em chol usando IQR e Z-score, quantos encontrou?](https://github.com/Leandro-Cardoso/univassouras-ciencia-de-dados/blob/main/atividade-03-Dataset-Saude/src/atividade_04.py)

5. [Faça um boxplot de thalach (frequência cardíaca máxima) por target (doença cardíaca).](https://github.com/Leandro-Cardoso/univassouras-ciencia-de-dados/blob/main/atividade-03-Dataset-Saude/src/atividade_05.py)

![Atividade 5](https://github.com/Leandro-Cardoso/univassouras-ciencia-de-dados/blob/main/atividade-03-Dataset-Saude/img/atividade_05.png)

6. [Calcule a correlação de Pearson entre todas as variáveis numéricas e visualize com heatmap.](https://github.com/Leandro-Cardoso/univassouras-ciencia-de-dados/blob/main/atividade-03-Dataset-Saude/src/atividade_06.py)

![Atividade 6](https://github.com/Leandro-Cardoso/univassouras-ciencia-de-dados/blob/main/atividade-03-Dataset-Saude/img/atividade_06.png)

7. [Teste com qui-quadrado se sex está associado a target.](https://github.com/Leandro-Cardoso/univassouras-ciencia-de-dados/blob/main/atividade-03-Dataset-Saude/src/atividade_07.py)

8. [Bônus: gere um pairplot e identifique o par com maior correlação.](https://github.com/Leandro-Cardoso/univassouras-ciencia-de-dados/blob/main/atividade-03-Dataset-Saude/src/atividade_08.py)

![Atividade 8](https://github.com/Leandro-Cardoso/univassouras-ciencia-de-dados/blob/main/atividade-03-Dataset-Saude/img/atividade_08.png)

* [**Atividades complementares**](https://github.com/Leandro-Cardoso/univassouras-ciencia-de-dados/blob/main/atividade-03-Dataset-Saude/src/atividade_complementar.ipynb)
