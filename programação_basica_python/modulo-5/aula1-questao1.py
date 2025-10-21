
numero1 = float(input("Por favor, insira o primeiro número decimal: "))
numero2 = float(input("Por favor, insira o segundo número decimal: "))

diferenca = abs(numero1 - numero2)

diferenca_arredondada = round(diferenca, 2)

print(f"\nA diferença absoluta entre {numero1} e {numero2} é: {diferenca_arredondada}")