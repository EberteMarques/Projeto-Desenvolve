import random

lista1 = []
lista2 = []

for _ in range(20):
    valor_aleatorio = random.randint(0, 50)
    lista1.append(valor_aleatorio)

    valor_aleatorio = random.randint(0, 50)
    lista2.append(valor_aleatorio)

set1 = set(lista1)
set2 = set(lista2)

interseccao_set = set1.intersection(set2)

lista_interseccao = list(interseccao_set)

print("Lista 1:", lista1)
print("Lista 2:", lista2)

lista_interseccao_ordenada = sorted(lista_interseccao)
print("A lista intersecção ordenada:", lista_interseccao_ordenada)

print("\nA quantidade de vezes que cada elemento da intersecção aparece em cada lista:")
for elemento in lista_interseccao_ordenada:
    contagem_lista1 = lista1.count(elemento)
    contagem_lista2 = lista2.count(elemento)
    print(f"{elemento}: (lista1={contagem_lista1}, lista2={contagem_lista2})")