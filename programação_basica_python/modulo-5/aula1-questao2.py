import random
import math

while True:
    
    n_str = input("Quantos números inteiros aleatórios você gostaria de gerar? ")
    n = int(n_str)
    if n <= 0:
         print("Por favor, insira um número inteiro positivo.")
    else:
            break
    
soma_dos_valores = 0
valores_gerados = []


print("\nValores gerados:")
for _ in range(n):
    valor_aleatorio = random.randint(0, 100)
    valores_gerados.append(valor_aleatorio)
    soma_dos_valores += valor_aleatorio
    print(valor_aleatorio)

raiz_quadrada_da_soma = math.sqrt(soma_dos_valores)

print(f"\nSoma dos valores gerados: {soma_dos_valores}")
print(f"Raiz quadrada da soma: {raiz_quadrada_da_soma:.2f}")