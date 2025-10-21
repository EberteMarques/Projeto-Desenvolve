import os
import re

arquivo_entrada = "frase.txt"
arquivo_saida = "palavras.txt"

caminho_entrada = os.path.join(os.path.dirname(os.path.abspath(__file__)), arquivo_entrada)
caminho_saida = os.path.join(os.path.dirname(os.path.abspath(__file__)), arquivo_saida)
   
with open(caminho_entrada, 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()

    
palavras_limpas = re.findall(r'[a-zA-Z]+', conteudo)
conteudo_formatado = "\n".join(palavras_limpas)

with open(caminho_saida, 'w', encoding='utf-8') as novo_arquivo:
    novo_arquivo.write(conteudo_formatado)


print("Conteúdo do arquivo 'palavras.txt':\n")
print(conteudo_formatado)
    
