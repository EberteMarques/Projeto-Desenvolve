import re

def eh_palindromo(frase):
 
  # Normaliza a frase: remove caracteres não alfabéticos e converte para minúsculo
  frase_normalizada = re.sub(r'[^a-zA-Z]', '', frase).lower()

  # Compara a frase normalizada com sua versão invertida
  return frase_normalizada == frase_normalizada[::-1]

# Inicia o loop do programa
while True:
  # Solicita a entrada do usuário
  frase_digitada = input('Digite uma frase (digite "fim" para encerrar): ')

  # Verifica a condição de saída
  if frase_digitada.lower() == 'fim':
    break

  # Verifica se a frase é um palíndromo e imprime o resultado
  if eh_palindromo(frase_digitada):
    print(f'"{frase_digitada}" é palíndromo')
  else:
    print(f'"{frase_digitada}" não é palíndromo')

print("Programa encerrado.")