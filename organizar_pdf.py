import pdfplumber
import re
import pandas as pd

# Função para extrair números no formato '5592984189641'
def extrair_numeros_telefone(texto):
    # Expressão regular para encontrar números no formato 559XXXXXXXXXX
    padrao = r'55\d{11}'
    return re.findall(padrao, texto)

# Abrir e ler o PDF
arquivo_pdf = 'export_calls_did - 2024-09-30T124817.316.pdf'
numeros_telefone = []

with pdfplumber.open(arquivo_pdf) as pdf:
    # Percorrer todas as páginas do PDF
    for pagina in pdf.pages:
        texto = pagina.extract_text()
        # Extrair números de telefone na página atual
        numeros_telefone += extrair_numeros_telefone(texto)

# Remover duplicatas, se houver
numeros_telefone = list(set(numeros_telefone))

# Criar um DataFrame com os números de telefone
df = pd.DataFrame(numeros_telefone, columns=['Telefone'])

# Salvar os números em um arquivo CSV
df.to_csv('telefones_extraidos.csv', index=False)

print("Números de telefone extraídos e salvos em 'telefones_extraidos.csv'.")
