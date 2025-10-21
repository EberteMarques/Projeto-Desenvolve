import random

numero_secreto = random.randint(1, 10)
palpite = 0

print("Bem-vindo ao jogo de adivinhação!")
print("Estou pensando em um número entre 1 e 10. Consegue adivinhar?")

while palpite != numero_secreto:
    
        palpite_str = input("Qual é o seu palpite? ")
        palpite = int(palpite_str)

        if palpite < numero_secreto:
            print("Muito baixo! Tente novamente.")
        elif palpite > numero_secreto:
            print("Muito alto! Tente novamente.")
        else:
            print(f"Parabéns! Você acertou! O número era {numero_secreto}.")
    