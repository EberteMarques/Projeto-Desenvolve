import random

def carregar_palavra():
    
     with open("gabarito_forca.txt", "r") as arquivo:
        palavras = arquivo.read().splitlines()
        return random.choice(palavras).upper()
  


def carregar_estagios():
    
    with open("gabarito_enforcado.txt", "r") as arquivo:
        estagios = arquivo.read().split("====\n")  # Separador entre estágios
    return estagios
   

# Função principal do jogo
def jogar_forca():
    palavra = carregar_palavra()
    estagios = carregar_estagios()
    letras_descobertas = ["_" for _ in palavra]
    letras_erradas = []
    tentativas_restantes = len(estagios) - 1

    print("Bem-vindo ao jogo da Forca!")
    while tentativas_restantes > 0 and "_" in letras_descobertas:
        print("\n" + estagios[len(estagios) - 1 - tentativas_restantes])
        print("Palavra: " + " ".join(letras_descobertas))
        print(f"Letras erradas: {', '.join(letras_erradas)}")
        print(f"Tentativas restantes: {tentativas_restantes}")

        chute = input("Digite uma letra: ").upper()
        if len(chute) != 1 or not chute.isalpha():
            print("Por favor, digite apenas uma letra válida.")
            continue

        if chute in letras_descobertas or chute in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        if chute in palavra:
            for i, letra in enumerate(palavra):
                if letra == chute:
                    letras_descobertas[i] = chute
            print("Boa! Você acertou uma letra.")
        else:
            letras_erradas.append(chute)
            tentativas_restantes -= 1
            print("Ops! Essa letra não está na palavra.")

    if "_" not in letras_descobertas:
        print("\nParabéns! Você venceu!")
        print("A palavra era:", palavra)
    else:
        print("\n" + estagios[-1])
        print("Você perdeu! A palavra era:", palavra)

# Executa o jogo
if __name__ == "__main__":
    jogar_forca()
