def contar_vogais_e_indices(frase):
  
  vogais = "aeiouAEIOU"
  indices = []
  contador_vogais = 0
  
  for i, letra in enumerate(frase):
    if letra in vogais:
      contador_vogais += 1
      indices.append(i)
      
  print(f"{contador_vogais} vogais")
  print(f"Índices {indices}")


frase_digitada = input("Digite uma frase: ")
contar_vogais_e_indices(frase_digitada)