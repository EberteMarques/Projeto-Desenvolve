import csv

# Nome do arquivo a ser lido
nome_arquivo = 'spotify-2023.csv'
# Parâmetro de codificação conforme solicitado
codificacao = 'latin-1'

# Abrindo o arquivo para leitura ('r') com a codificação especificada
# Se o arquivo não existir, ocorrerá um FileNotFoundError aqui.
with open(nome_arquivo, mode='r', encoding=codificacao) as arquivo_csv:
    # Criando um leitor de CSV
    leitor_csv = csv.reader(arquivo_csv)

    print(f"--- Primeiras 5 linhas do arquivo '{nome_arquivo}' (com codificação '{codificacao}') ---")

    # Variável para contar as linhas que já foram impressas
    contador_linhas = 0

    # Iterando sobre as linhas do arquivo
    for linha in leitor_csv:
        # Imprime a linha (que é uma lista de strings)
        print(linha)

        # Incrementa o contador
        contador_linhas += 1

        # Verifica se já imprimiu 5 linhas
        if contador_linhas >= 5:
            break # Sai do loop após imprimir a quinta linha

    print("--- Leitura finalizada. ---")