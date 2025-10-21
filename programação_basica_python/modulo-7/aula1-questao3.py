def contar_espacos(frase):
  
  contador = 0
  for caractere in frase:
    if caractere == ' ':
      contador += 1
  return contador

frase_do_usuario = input("Digite uma frase para contar os espaços: ")
numero_de_espacos = contar_espacos(frase_do_usuario)
print(f"A frase '{frase_do_usuario}' tem {numero_de_espacos} espaços em branco.")