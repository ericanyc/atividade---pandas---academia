import pandas as pd

dados = pd.read_csv("academia.csv")

print("=== Parte 3 - Exploração Inicial ===")
print("Primeiras 5 linhas:")
print(dados.head())

print("\nÚltimas 5 linhas:")
print(dados.tail())

print("\nTotal de linhas e colunas:")
print(dados.shape)

print("\n=== Parte 4 - Estatísticas Básicas ===")
print("Média das idades dos alunos:")
print(dados['Idade'].mean())