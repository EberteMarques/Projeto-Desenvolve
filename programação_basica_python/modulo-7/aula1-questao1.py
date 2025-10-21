def imprimir_escada():
  nome = input("Digite seu nome: ")
  for i in range(len(nome)):
    print(nome[:i+1])

imprimir_escada()