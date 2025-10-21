#Você está implementando um sistema de entrega expressa e precisa calcular o valor do frete com base na distância e no peso do pacote. Escreva um código que solicita a distância da entrega em quilômetros e o peso do pacote em quilogramas. O programa deve calcular e imprimir o valor do frete de acordo com as seguintes regras:

#Distância até 100 km: R$1 por kg.
#Distância entre 101 e 300 km: R$1.50 por kg.
#Distância acima de 300 km: R$2 por kg.
#Acrescente uma taxa de R$10 para pacotes com peso superior a 10 kg

distancia = float(input("Digite a distância da entrega em km: "))
peso = float(input("Digite o peso do pacote em kg: "))

if distancia <= 100:
    valor_frete_base = 1.00 * peso
elif 101 <= distancia <= 300:
    valor_frete_base = 1.50 * peso
else:
    valor_frete_base = 2.00 * peso
if peso > 10:
    valor_frete_final = valor_frete_base + 10.00
else:
    valor_frete_final = valor_frete_base
print(f"O valor total do frete é: R${valor_frete_final:.2f}")