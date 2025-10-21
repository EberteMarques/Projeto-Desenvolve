#Você está criando um sistema de classificação de filmes com base nas avaliações dos usuários. Escreva um programa em Python que solicita ao usuário para inserir a avaliação de um filme em uma escala de 1 a 5. O programa deve imprimir uma mensagem correspondente à classificação do filme:

#Se a avaliação for 5, imprima "Excelente!"
#Se a avaliação for 4, imprima "Muito Bom!"
#Se a avaliação for 3, imprima "Bom!"
#Se a avaliação for 2, imprima "Regular."
#Se a avaliação for 1, imprima "Ruim."

print("###"*11)
print("Sistema de classificação de filmes")
print("###"*11)

a = int(input(" De 1 à 5 digite o seu grau de satisfação em relação ao filme, onde 5 é 'EXCELENTE' e 1 'RUIM':"))

if a == 1:
    print("+++"*11)
    print("Na sua avaliação o filme foi: Ruim")
    print("+++"*11)
elif a == 2:
    print("+++"*11)
    print("Na sua avaliação o filme foi: Regular")
    print("+++"*11)
elif a == 3:
    print("+++"*11)
    print("Na sua avaliação o filme foi: Bom!")
    print("+++"*11)
elif a == 4:
    print("+++"*11)
    print("Na sua avaliação o filme foi: Muito Bom!")
    print("+++"*11)
else:
    print("+++"*11)
    print("Na sua avaliação o filme foi: Excelente!")
    print("+++"*11)

print("FIM")

