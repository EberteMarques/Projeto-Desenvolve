import os

frase = input("Digite uma frase: ")


nome_arquivo = "frase.txt"

caminho_completo = os.path.join(os.path.dirname(os.path.abspath(__file__)), nome_arquivo)

with open(caminho_completo, 'w', encoding='utf-8') as arquivo:
    arquivo.write(frase)

print(f"Frase salva em {caminho_completo}")