n = int(input("Digite o número de idades para ser calculado a média: "))

soma = 0
cont = 1
while cont <= n:
    idade = int(input(f"digite a idade nº {cont}: "))
    soma += idade
    cont += 1
print(f"A soma das idades é: {soma}, e sua média é: {soma/n}")