
a, b, c = int(input("Digite o valor referente a 'a':")), int(input("Digite o valor referente a 'b':")), int(input("Digite o valor referente a 'c':"))
delta = b**2 - 4*a*c
if delta > 0:
    raiz1 = (-b + delta**(1/2))/(2*a)
    raiz2 = (-b - delta**(1/2))/(2*a)
    print(raiz1, raiz2)

else:
    print("Não tem raizes reais")
    