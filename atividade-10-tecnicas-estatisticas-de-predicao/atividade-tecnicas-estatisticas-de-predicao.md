# Atividade: Resolvendo um Problema Real

## 1. O que fazer

Escolha um problema real (do seu trabalho, da sua rotina, de uma área que você conhece, ou de um caso público que você possa explicar) em que valha a pena prever um valor desconhecido (Y) a partir de informações conhecidas (X) — ou seja, um problema de regressão (Y contínuo: preço, nota, tempo, salário...) ou de classificação binária (Y categórico: sim/não, cancela/não cancela, aprova/reprova...).

Tema é livre. A única exigência é que o problema seja real (ou realista — pode usar dados fictícios coerentes, desde que o problema em si faça sentido) e que faça sentido aplicar um modelo preditivo supervisionado a ele.

## 2. Regras obrigatórias

### 2.1 Modelo preditivo — lista fechada, escolha só um

Permitido nesta atividade	Y é...

Regressão Linear Simples (1 preditor)	contínuo

Regressão Linear Múltipla (2+ preditores)	contínuo

Regressão Logística	binário (0/1, sim/não)

Não use Árvore de Decisão, Random Forest, KNN, SVM, Redes Neurais, Gradient Boosting/XGBoost ou qualquer outro modelo. Esses nomes apareceram na aula de hoje só como panorama ("outros métodos populares") — ainda não foram implementados passo a passo e ficam para as Aulas 10 e 11. A própria Aula 09 trouxe a regra que vale aqui: comece sempre pelo modelo mais simples que resolve o problema.

### 2.2 Aulas e conceitos obrigatórios

Use conceitos da Aula 09 (Predição) + pelo menos 2 outras aulas, entre as Aulas 01 a 08 (Big Data, Python, Estatística Descritiva, Probabilidade, Inferência, Visualização/NoSQL, Mineração de Dados, Ética/Qualidade de Dados). Diga explicitamente quais aulas e quais conceitos de cada uma você usou.

Importante — as aulas anteriores não são enfeite, são pré-requisito para a predição funcionar/valer a pena. Mostre essa conexão, não apenas liste as aulas. Exemplos do que conta como uso real:

* Aula 03 (Estatística Descritiva): olhar média/dispersão e a correlação entre X e Y antes de ajustar a regressão — se não há relação nenhuma, o modelo não vai servir de nada.
* Aula 08 (Qualidade de Dados): tratar nulos, duplicatas e valores impossíveis antes de treinar o modelo — um outlier não tratado distorce a reta inteira.
* Aula 05 (Inferência): avaliar se o coeficiente encontrado é estatisticamente significativo, ou se pode ser efeito do acaso em uma amostra pequena.
* Aula 02 (Python): organização do código (funções/POO) usada para separar preparo dos dados, treino e avaliação do modelo.

### 2.3 Uso de Inteligência Artificial (obrigatório, mesmo protocolo do exercício anterior)

Registre:

* O que você perguntou/pediu à IA (o prompt).
* O que ela respondeu (resumido).
* O que você teve que corrigir, completar ou rejeitar na resposta da IA, e por quê. Se ela acertou tudo de primeira, explique como você verificou isso.

### 2.4 Simplicidade (critério de avaliação, não sugestão)

Um único modelo (da lista em 2.1), poucos preditores, divisão treino/teste simples (ex.: 80/20) e as métricas padrão apresentadas em aula — MAE, RMSE e R² para regressão, ou acurácia/matriz de confusão para logística. Empilhar técnica não ensinada ainda (mesmo que você já conheça de fora) é penalizado, não premiado.

### 2.5 Pergunta obrigatória (Parte 5)
Responda sem apoio de IA. Ver seção 3.

## 3. Pergunta obrigatória
Explique, com suas próprias palavras, qual foi a principal técnica/conceito que você aplicou neste exercício (incluindo qual modelo preditivo escolheu e por quê) e por que ela resolve o problema que você escolheu. Em seguida, avalie seu próprio nível de entendimento sobre essa técnica (iniciante, intermediário ou avançado) e justifique com um exemplo prático — não basta dizer o nível, mostre com um pequeno exemplo ou situação que comprove esse entendimento. Por fim, cite um ponto em que você teve que questionar ou corrigir a resposta da IA, e como percebeu que precisava fazer isso.

## 4. Estrutura da entrega (.ipynb, .py, PDF ou Word)

Parte	Conteúdo

1. Problema real escolhido e por que ele importa (contexto)
2. Dados usados (origem/amostra) + quais aulas/conceitos foram aplicados (Aula 09 + pelo menos 2 outras)
3. Desenvolvimento: preparo dos dados apoiado nas aulas anteriores → divisão treino/teste → modelo preditivo (da lista em 2.1) → avaliação com as métricas da Aula 09
4. Registro do uso de IA: prompt, resposta, e o que você corrigiu/validou
5. Resposta à pergunta obrigatória (sem IA)
6. Conclusão: o que a predição significa para o problema real, e algum limite do modelo (ex.: cuidado com extrapolação fora do intervalo dos dados de treino, como visto em aula)

## 5. Critérios de avaliação (1 pontos)

| Critério | Pontos |
| --- | --- |
| Problema real bem definido e relevante | 0,15 |
| Aplicação correta de Aula 09 + 2 outras aulas (explicitamente identificadas), com modelo dentro da lista permitida e métricas coerentes | 0,30 |
| Uso documentado e crítico de IA (não cópia cega) | 0,20 |
| Simplicidade e clareza da solução (penaliza modelo fora da lista ou técnica não ensinada) | 0,15 |
| Resposta à pergunta obrigatória de autoavaliação | 0,20 |
| Total | 1,0 |
