import pandas as pd
import re

# Função para formatar o número de telefone
def formatar_telefone(telefone):
    # Remove qualquer caractere que não seja número
    telefone_formatado = re.sub(r'\D', '', str(telefone))
    
    # Adiciona o prefixo '55' se ainda não tiver
    if not telefone_formatado.startswith('55'):
        telefone_formatado = '55' + telefone_formatado
    
    return telefone_formatado

# Ler o arquivo CSV com os números de telefone
df = pd.read_csv('telefones.csv')

# Aplicar a função de formatação à coluna 'Telefone'
df['telefone'] = df['telefone'].apply(formatar_telefone)

# Exibir os números de telefone formatados
print(df)

# Salvar o CSV com os números formatados
df.to_csv('telefones_formatados.csv', index=False)

print("Números de telefone formatados e salvos em 'telefones_formatados.csv'.")
