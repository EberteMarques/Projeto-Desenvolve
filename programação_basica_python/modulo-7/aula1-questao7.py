import random

def encrypt(nomes):
    
    # 1. Gera a chave de criptografia aleatória entre 1 e 10
    chave = random.randint(1, 10)
    
    nomes_criptografados = []
    
    # 2. Itera sobre cada nome na lista
    for nome in nomes:
        nome_criptografado = ""
        # 3. Itera sobre cada caractere do nome
        for char in nome:
            # Pega o valor Unicode do caractere
            unicode_valor = ord(char)
            # Adiciona a chave
            novo_unicode = unicode_valor + chave
            
            # Garante que o caractere permaneça no intervalo visível (33 a 126)
            # Se exceder 126, "volta" para o início do intervalo
            if novo_unicode > 126:
                novo_unicode = 33 + (novo_unicode - 127)
            
            nome_criptografado += chr(novo_unicode)
            
        nomes_criptografados.append(nome_criptografado)
        
    return nomes_criptografados, chave

lista_nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_cifrados, chave_cifrada = encrypt(lista_nomes)

print(f"Nomes originais: {lista_nomes}")
print(f"Nomes criptografados: {nomes_cifrados}")
print(f"Chave de criptografia: {chave_cifrada}")