#print("Digite os números que você quer testar")
#n1 = int(input())
#n2 = int(input())
#n3= n1+n2

#if n3 % 2 == 0:
#    print( f"a soma de {n1} com {n2} é {n3}, sendo assim, é un número par!!")
#else:
#    print( f"a soma de {n1} com {n2} é {n3}, sendo assim, é un número impar!!")

print("Digite os números que você quer testar")
n1, n2 = int(input()), int(input())
print(f"a soma de {n1} com {n2} é {n1+n2}, sendo assim, é un número par!!" if n1+n2 % 2 == 0 else f"a soma de {n1} com {n2} é {n1+n2}, sendo assim, é un número impar!!")
