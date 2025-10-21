print("="*30)
print("sistema de cálculo de medias")
print("=" *30)


print("DIGITE TRêS NOTAS")


n1 = float(input("digite a primeira nota: "))
n2 = float(input("digite a segunda nota: "))
n3 = float(input("digite a terceira nota: "))

m = (n1+n2+n3)/3

if m >= 60:
    print("Aprovado!")
elif m >= 40:
    print("Recuperação")
else:
    print("Reprovado!")


print("Fim")