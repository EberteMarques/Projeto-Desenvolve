n = int(input("Digite a quantidade de experimentos: "))
cont = 1
a, b, c, = "sapo", "rato", "coelho"
sapo, rato, coelho = 0, 0, 0

while cont <= n:
    tipo = input(f"Digite o tipo de cobaia '{a}, {b}, ou {c}': ")
    quantia = int(input(f"Digita o valor unitário de {tipo}: "))

    if tipo == a:
        sapo += quantia

    elif tipo == b:
        rato += quantia

    elif tipo == c:
        coelho += quantia

    cont += 1

    total = sapo + rato + coelho

print("O tota de cobaias foi: ", total)
print(f"O total de {a} foi: {sapo} ")
print(f"O total de {b} foi: {rato} ")
print(f"O total de {c} foi: {coelho} ")

print(f"O percentual de {a} é: ", total/sapo)
print(f"O percentual de {b} é: ", total/rato)
print(f"O percentual de {c} é: ", total/coelho)