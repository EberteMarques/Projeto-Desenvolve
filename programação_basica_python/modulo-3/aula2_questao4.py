classe = str(input("Escolha a classe do personagem:( guerreiro, mago ou arqueiro): "))

pf = int(input(f"Digite os pontos de força para o personagem {classe} (de 1 à 20): "))

ma = int(input(f" Digite os pontos de magia para {classe}( de 1 à 20): "))

guerreiro =  pf >= 15 and ma <=10
mago =  pf <= 10 and ma >=15
arqueiro =  pf >= 5 <=15 and ma >=5 <=15
