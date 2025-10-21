import random

num_elementos = random.randint(5, 20)

elementos = []
for _ in range(num_elementos):
    valor = random.randint(1, 10)
    elementos.append(valor)

print("A lista elementos:", elementos)

soma_valores = sum(elementos)
print("A soma dos valores da lista é:", soma_valores)

media_valores = soma_valores / len(elementos)
print("A média dos valores da lista é:", media_valores)