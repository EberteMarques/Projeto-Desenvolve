frase_usuario = input("Digite uma frase: ")

frase_processada = frase_usuario.lower()

vogais_referencia = "aeiouáàãâéêíóôõúü"

lista_vogais = sorted([caractere for caractere in frase_processada if caractere in vogais_referencia])
print(f"Vogais: {lista_vogais}")

lista_consoantes = [caractere for caractere in frase_processada if caractere not in vogais_referencia and caractere.isalpha() and not caractere.isspace()]
print(f"Consoantes: {lista_consoantes}")