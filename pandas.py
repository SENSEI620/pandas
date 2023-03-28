import pandas as pd

# lê o arquivo CSV com os dados
dados = pd.read_csv('dados.csv')

# cria uma coluna "total" que é a soma das colunas "receita" e "custo"
dados['total'] = dados['receita'] - dados['custo']

# agrupa os dados por "ano" e "mes" e calcula a média do total para cada grupo
media_por_mes = dados.groupby(['ano', 'mes'])['total'].mean()

# imprime a média de cada mês
print(media_por_mes)
