import pandas as pd
import os

# Ler o arquivo CSV
df = pd.read_csv('telefones.csv')

# Contar o número total de telefones
numero_de_telefones = df['telefone'].count()
print(f"Total de telefones: {numero_de_telefones}")

# Dividir os telefones em arquivos de 2000 linhas
tamanho_por_arquivo = 2000
num_arquivos = (numero_de_telefones // tamanho_por_arquivo) + (numero_de_telefones % tamanho_por_arquivo > 0)

# Criar uma pasta para armazenar os arquivos se não existir
os.makedirs('telefones_divididos', exist_ok=True)

# Dividir e salvar os telefones em múltiplos arquivos
for i in range(num_arquivos):
    df_dividido = df.iloc[i * tamanho_por_arquivo:(i + 1) * tamanho_por_arquivo]
    df_dividido.to_csv(f'telefones_divididos/telefones_{i + 1}.csv', index=False)

print(f"Telefones divididos em {num_arquivos} arquivos, cada um contendo até {tamanho_por_arquivo} números.")
