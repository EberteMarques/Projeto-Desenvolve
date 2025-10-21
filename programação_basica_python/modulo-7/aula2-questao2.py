def substituir_vogais(frase):
  vogais = "aeiouAEIOU"
  nova_frase = ""
  
  # Itera por cada caractere da frase original
  for caractere in frase:
    # Verifica se o caractere é uma vogal
    if caractere in vogais:
      # Se for, adiciona um asterisco à nova frase
      nova_frase += "*"
    else:
      # Se não for, adiciona o próprio caractere à nova frase
      nova_frase += caractere
      
  return nova_frase

# Solicita a frase ao usuário
frase_original = input("Digite uma frase: ")

# Chama a função para modificar a frase
frase_modificada = substituir_vogais(frase_original)

# Imprime o resultado
print(f"Frase modificada: {frase_modificada}")