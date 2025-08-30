import pandas as pd

# ----- Passo 1: Importar os CSVs -----
csv_ia = "Dilema Ético IA(IA).csv"          # caminho do CSV da IA
csv_humano = "Dilema Ético IA(Pessoas).csv"  # caminho do CSV dos humanos

# Importando CSV da IA
df_ia = pd.read_csv(csv_ia)
df_ia = df_ia.dropna(how='all')  # remove linhas totalmente vazias
df_ia = df_ia.rename(columns={
    '1\n': 'Q1',
    '2\n': 'Q2',
    '3': 'Q3',
    '4': 'Q4',
    '5': 'Q5'
})
df_ia = df_ia[['Id', 'Email', 'Q1', 'Q2', 'Q3', 'Q4', 'Q5']]
df_ia['Grupo'] = 'IA'

# Importando CSV dos Humanos
df_humano = pd.read_csv(csv_humano)
df_humano = df_humano.dropna(how='all')
# Renomear colunas longas para Q1-Q5
df_humano = df_humano.rename(columns={
    'Você acha que sistemas de IA em recrutamento podem ser injustos ou preconceituosos? Por quê?\n': 'Q1',
    'Se um algoritmo rejeitasse sua candidatura, você gostaria de saber os motivos?\n': 'Q2',
    'Na sua opinião, usar IA em processos seletivos aumenta ou diminui as oportunidades para mulheres e minorias?\n': 'Q3',
    'Quem deve ser responsável se a IA cometer um erro em um processo seletivo?\n': 'Q4',
    'Você participaria de um processo seletivo totalmente automatizado por IA?\n': 'Q5'
})
df_humano = df_humano[['Id', 'Email', 'Q1', 'Q2', 'Q3', 'Q4', 'Q5']]
df_humano['Grupo'] = 'Humano'

# ----- Passo 2: Unir os dois datasets -----
df_total = pd.concat([df_ia, df_humano], ignore_index=True)

# ----- Passo 3: Visualizar o dataset consolidado -----
print(df_total.head())

# ----- Salvar CSV consolidado -----
df_total.to_csv("consolidado.csv", index=False)








