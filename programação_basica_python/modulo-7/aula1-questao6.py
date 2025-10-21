def encontrar_anagramas(frase, palavra_objetivo):
 
  # Cria a assinatura da palavra objetivo
  assinatura_objetivo = sorted(palavra_objetivo.lower())
  
  # Lista para armazenar os anagramas encontrados
  anagramas_encontrados = []
  
  # Divide a frase em palavras
  palavras = frase.split()
  
  for palavra in palavras:
    # Remove pontuação e normaliza a palavra para comparação
    palavra_limpa = ''.join(filter(str.isalpha, palavra))
    palavra_normalizada = palavra_limpa.lower()
    
    # Cria a assinatura da palavra atual
    assinatura_atual = sorted(palavra_normalizada)
    
    # Compara as assinaturas
    if assinatura_atual == assinatura_objetivo:
      anagramas_encontrados.append(palavra)
      
  return anagramas_encontrados

frase = input("Digite uma frase: ")
palavra = input("Digite a palavra objetivo: ")

resultado = encontrar_anagramas(frase, palavra)

print(f"Anagramas: {resultado}")