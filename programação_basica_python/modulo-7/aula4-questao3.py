import os
import re

# Define o nome do arquivo
nome_arquivo = "estomago.txt"

# Cria o caminho completo para o arquivo
caminho_completo = os.path.join(os.path.dirname(os.path.abspath(__file__)), nome_arquivo)

# Abre o arquivo com a codificação 'latin-1'
with open(caminho_completo, 'r', encoding='latin-1') as arquivo:
    linhas = arquivo.readlines()
    
print("--- As primeiras 25 linhas do texto ---")
for linha in linhas[:25]:
    print(linha.strip())
    
print("\n--- Número de linhas ---")
num_linhas = len(linhas)
print(f"O arquivo tem {num_linhas} linhas.")
    
print("\n--- Linha com mais caracteres ---")
linha_maior = max(linhas, key=len)
print(f"A linha com o maior número de caracteres é:")
print(linha_maior.strip())
    
print("\n--- Contagem de personagens ---")
texto_completo = "".join(linhas)
mencoes_nonato = len(re.findall(r'\bNonato\b', texto_completo, re.IGNORECASE))
mencoes_iria = len(re.findall(r'\bÍria\b', texto_completo, re.IGNORECASE))
    
print(f"O nome 'Nonato' é mencionado {mencoes_nonato} vezes.")
print(f"O nome 'Íria' é mencionado {mencoes_iria} vezes.")