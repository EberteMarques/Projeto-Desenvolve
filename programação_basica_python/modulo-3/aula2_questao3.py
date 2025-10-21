nome = str(input("qual é o seu nome: "))

id = int(input(f"Qual sua idade {nome}? "))

j = int(input(f"{nome} você já jogou pelo menos 3 jogos de tabuleiro? digite '1' para sim '2' para não: "))

v = int(input(f"Me diga uma coisa {nome}, quantos jogos você já vence? "))

r = id >= 16 and id <=18 and j == 2 and v >=3

print(f"A informação que {nome} está apto para ingressar no clube de jogos de tabuleiro é {r}!")