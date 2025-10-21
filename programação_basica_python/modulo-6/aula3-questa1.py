numeros = []

print("Por favor, digite números inteiros para adicionar à lista.")
print("Você pode digitar 'fim' a qualquer momento para parar,")
print("mas a lista deve ter pelo menos 4 números para que o programa prossiga.")

while True:
    entrada = input("Digite um número inteiro (ou 'fim' para parar): ")

    if entrada.lower() == 'fim':
        if len(numeros) >= 4:
            break
        else:
            print("A lista deve ter pelo menos 4 valores. Por favor, continue adicionando números.")
    else:
        numero = int(entrada)
        numeros.append(numero)


print(f"A lista original: {numeros}")

print(f"Os 3 primeiros elementos: {numeros[:3]}")

print(f"Os 2 últimos elementos: {numeros[-2:]}")

print(f"A lista invertida: {numeros[::-1]}")

print(f"Os elementos de índice par (0, 2, 4...): {numeros[::2]}")

print(f"Os elementos de índice ímpar (1, 3, 5...): {numeros[1::2]}")