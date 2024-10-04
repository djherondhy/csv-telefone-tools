import pandas as pd

# Ler os três arquivos CSV
df1 = pd.read_csv('telefones_sem_duplicatas.csv')
df2 = pd.read_csv('telefones_sem_duplicatas_2.csv')
df3 = pd.read_csv('telefones_sem_duplicatas_3.csv')

# Concatenar os DataFrames
df_concatenado = pd.concat([df1, df2, df3], ignore_index=True)

# Remover duplicatas na coluna 'Telefone'
df_sem_duplicatas = df_concatenado.drop_duplicates(subset=['telefone'])

# Salvar o DataFrame sem duplicatas em um novo arquivo CSV
df_sem_duplicatas.to_csv('all_telefones.csv', index=False)

print("Telefones dos três arquivos foram juntados e duplicatas removidas. Resultado salvo em 'telefones_juntos.csv'.")
