nome_arquivo = "usuarios.txt"
#retorna verdade se o usuário existe no arquivo
#e falso caso contrário

def verifica_usuario(usuario):
    with open(nome_arquivo, 'a+') as fp:
        fp.seek(0) # Move o ponteiro para o início do arquivo

        for linha in fp:
            if usuario == linha.strip(): # Remove espaços e quebras de linha

                return True
    return False 
                 
def cadastrar_usuario():
    nome_usuario = input('Digite seu novo usuário: ')

    if verifica_usuario(nome_usuario):
        print('Usuário já existe! Cadastro não realizado')
    else:
        with open(nome_arquivo, 'a') as fp:
            fp.write(nome_usuario +'\n')
        print('Cadastro realizado com sucesso!')


def fazer_login():
    nome_usuario = input('Digite seu usuário: ')
    if verifica_usuario(nome_usuario):
        print('Login realizado com sucesso!')
    else:
        print('Usuário incorreto!')
    

#programa principal

while True:
    print('1-Cadastrar\n2-Login\n3-Sair')
    op = int(input('Escolha uma opção: '))

    if op == 1:
        cadastrar_usuario()
    elif op == 2:
        fazer_login()
    elif op == 3:
        break
    else:
        print('++'*20)
        print('Opção inválida')
        
    