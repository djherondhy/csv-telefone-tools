import pandas as pd
import re

# Função para extrair e formatar números de telefone
def extrair_telefone(telefone):
    # Remove qualquer caractere que não seja número
    telefone_formatado = re.sub(r'\D', '', str(telefone))
    
    # Adiciona o prefixo '55' se ainda não tiver
    if not telefone_formatado.startswith('55'):
        telefone_formatado = '55' + telefone_formatado
    
    return telefone_formatado

# Ler o arquivo Excel
arquivo_excel = 'NUMEROS PARCIAIS DE MANAUS.xlsx'
df = pd.read_excel(arquivo_excel)

# Extrair a segunda coluna (índice 1) que contém os números de telefone
df['Telefone'] = df.iloc[:, 1].apply(extrair_telefone)

# Exibir os números de telefone formatados
print(df['Telefone'])

# Salvar os números de telefone extraídos em um novo CSV
df[['Telefone']].to_csv('telefones_formatados_2.csv', index=False)

print("Números de telefone extraídos e salvos em 'telefones_formatados.csv'.")
