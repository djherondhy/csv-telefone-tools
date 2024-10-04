import pandas as pd

# Ler o arquivo CSV
df = pd.read_csv('telefones_formatados_2.csv')

# Remover duplicatas da coluna 'Telefone'
df_sem_duplicatas = df.drop_duplicates(subset=['Telefone'])

# Exibir o DataFrame sem duplicatas
print(df_sem_duplicatas)

# Salvar o DataFrame sem duplicatas em um novo arquivo CSV
df_sem_duplicatas.to_csv('telefones_sem_duplicatas_3.csv', index=False)

print("Telefones duplicados removidos e salvos em 'telefones_sem_duplicatas.csv'.")
