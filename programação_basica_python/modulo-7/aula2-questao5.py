import random

def embaralhar_palavras(frase):
 
  # Divide a frase em palavras
  palavras = frase.split()
  
  palavras_embaralhadas = []
  
  # Itera sobre cada palavra da lista
  for palavra in palavras:
    # Se a palavra tiver 3 ou mais caracteres, embaralha as letras internas
    if len(palavra) > 2:
      # Pega o primeiro e o último caractere
      primeira_letra = palavra[0]
      ultima_letra = palavra[-1]
      
      # Pega os caracteres internos, converte para lista para embaralhar
      meio = list(palavra[1:-1])
      
      # Embaralha a lista de caracteres internos
      random.shuffle(meio)
      
      # Junta a palavra novamente: primeiro + meio embaralhado + último
      palavra_nova = primeira_letra + "".join(meio) + ultima_letra
      palavras_embaralhadas.append(palavra_nova)
    else:
      # Se a palavra for muito curta, adiciona-a sem modificação
      palavras_embaralhadas.append(palavra)
      
  # Junta todas as palavras embaralhadas de volta em uma frase
  return " ".join(palavras_embaralhadas)

# Exemplo de uso:
frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)

