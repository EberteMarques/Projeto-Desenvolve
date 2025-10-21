# Lista com os nomes dos meses
meses = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

# Solicita a data de nascimento do usuário
data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")

# Divide a string da data em dia, mês e ano
# O método split('/') cria uma lista com os elementos separados pela barra
dia, mes, ano = data_nascimento.split('/')

# Converte a string do mês para um número inteiro e subtrai 1 para acessar a lista
# A lista de meses começa no índice 0 (Janeiro)
indice_mes = int(mes) - 1

# Pega o nome do mês na lista usando o índice
nome_mes = meses[indice_mes]

# Imprime a data formatada
print(f"Você nasceu em {dia} de {nome_mes} de {ano}.")