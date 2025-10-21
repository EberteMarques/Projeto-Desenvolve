# Abre (ou cria) o arquivo 'meus_livros.csv' no modo de escrita
with open('meus_livros.csv', 'w', encoding='utf-8') as arquivo:
    # Aqui você pode escrever no arquivo usando arquivo.write()
    arquivo.write('Título,Autor,Ano\n')  # Exemplo de cabeçalho CSV
