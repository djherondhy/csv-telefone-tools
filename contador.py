import pandas as pd

# Ler o arquivo CSV
df = pd.read_csv('telefones.csv')

# Contar o número de itens não nulos na coluna 'Telefone'
numero_de_itens = df['telefone'].count()

# Exibir a contagem
print(f"Total de itens na coluna 'Telefone' (não nulos): {numero_de_itens}")

# Para contar todos os itens, incluindo nulos, use .size
total_itens_incluindo_nulos = df['telefone'].size
print(f"Total de itens na coluna 'Telefone' (incluindo nulos): {total_itens_incluindo_nulos}")
