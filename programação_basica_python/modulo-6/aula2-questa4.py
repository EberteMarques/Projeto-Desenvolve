num_elementos1 = int(input("Digite a quantidade de elementos da lista 1: "))
lista1 = []
print("Digite os", num_elementos1, "elementos da lista 1:")
for _ in range(num_elementos1):
    valor = int(input())
    lista1.append(valor)

num_elementos2 = int(input("Digite a quantidade de elementos da lista 2: "))
lista2 = []
print("Digite os", num_elementos2, "elementos da lista 2:")
for _ in range(num_elementos2):
    valor = int(input())
    lista2.append(valor)

lista_intercalada = []

len1 = len(lista1)
len2 = len(lista2)
min_len = min(len1, len2)

for i in range(min_len):
    lista_intercalada.append(lista1[i])
    lista_intercalada.append(lista2[i])

if len1 > len2:
    lista_intercalada.extend(lista1[min_len:])
elif len2 > len1:
    lista_intercalada.extend(lista2[min_len:])

print("Lista intercalada:", *lista_intercalada)