# Exercício Prático

Cenário: Análise de Vendas de Supermercado
Dataset CSV com 1.000 transações. Use Python + Pandas + Matplotlib para explorar os dados.

## Colunas do Dataset

```py
"Branch"         # Filial (A, B, C)
"City"           # Cidade
"Customer type"  # Member / Normal
"Gender"         # Male / Female
"Product line"   # Categoria
"Unit price"     # Preço unitário
"Quantity"       # Quantidade
"Total"          # Total da venda
"Payment"        # Forma de pagamento
"Rating"         # Avaliação (1–10)
```

## Atividades

1. [Carregue o arquivo supermarket_sales.csv com Pandas e exiba as 5 primeiras linhas.](https://github.com/Leandro-Cardoso/univassouras-ciencia-de-dados/blob/main/atividade-02-Supermercado/src/atividade_01.py)

2. [Inspecione tipos de dados, dimensões e valores nulos.](https://github.com/Leandro-Cardoso/univassouras-ciencia-de-dados/blob/main/atividade-02-Supermercado/src/atividade_02.py)

3. [Calcule o total de vendas por filial (Branch) usando groupby.](https://github.com/Leandro-Cardoso/univassouras-ciencia-de-dados/blob/main/atividade-02-Supermercado/src/atividade_03.py)

4. Identifique a linha de produto com maior ticket médio.

5. Crie um gráfico de barras comparando o faturamento por filial.

6. Plote a distribuição da avaliação (Rating) com histograma + KDE.

7. Bônus: correlacione Total e Rating com scatter plot.
