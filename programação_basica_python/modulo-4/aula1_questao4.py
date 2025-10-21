n = int(input())
maior = 0
while n > 0:
    x = int(input("Digite um valor: "))
    if x > maior:
        maior = x
    else:
        n = n - 1
print(maior)