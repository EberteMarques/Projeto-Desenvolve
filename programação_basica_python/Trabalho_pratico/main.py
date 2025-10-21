import csv

# Carregar usuários
def carregar_usuarios():
    usuarios = {}
    with open('usuarios.csv', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for linha in reader:
            id, nome, login, senha, categoria = linha
            usuarios[login] = {
                'id': id,
                'nome': nome,
                'senha': senha,
                'categoria': categoria
            }
    return usuarios

# Carregar produtos/serviços
def carregar_produtos():
    produtos = []
    with open('produtos.csv', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for linha in reader:
            id, nome, tipo, preco, quantidade = linha
            produtos.append({
                'id': id,
                'nome': nome,
                'tipo': tipo,
                'preco': float(preco),
                'quantidade': int(quantidade)
            })
    return produtos

# Login
def login(usuarios):
    user = input("Login: ")
    senha = input("Senha: ")
    if user in usuarios and usuarios[user]['senha'] == senha:
        return usuarios[user]
    else:
        print("Login inválido.")
        return None

# CRUD de usuários
def cadastrar_usuario():
    with open('usuarios.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        id = input("ID: ")
        nome = input("Nome: ")
        login = input("Login: ")
        senha = input("Senha: ")
        categoria = input("Categoria: ")
        writer.writerow([id, nome, login, senha, categoria])
        print("Usuário cadastrado.")

def listar_usuarios():
    with open('usuarios.csv', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for linha in reader:
            print(linha)

def atualizar_usuario():
    login_alvo = input("Login do usuário a atualizar: ")
    usuarios = carregar_usuarios()
    if login_alvo in usuarios:
        usuarios[login_alvo]['nome'] = input("Novo nome: ")
        usuarios[login_alvo]['categoria'] = input("Nova categoria: ")
        with open('usuarios.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            for u in usuarios.values():
                writer.writerow([u['id'], u['nome'], login_alvo, u['senha'], u['categoria']])
        print("Usuário atualizado.")
    else:
        print("Usuário não encontrado.")

def remover_usuario():
    login_alvo = input("Login do usuário a remover: ")
    usuarios = carregar_usuarios()
    if login_alvo in usuarios:
        del usuarios[login_alvo]
        with open('usuarios.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            for login, u in usuarios.items():
                writer.writerow([u['id'], u['nome'], login, u['senha'], u['categoria']])
        print("Usuário removido.")
    else:
        print("Usuário não encontrado.")

# CRUD de produtos/serviços
def cadastrar_produto():
    with open('produtos.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        id = input("ID: ")
        nome = input("Nome: ")
        tipo = input("Tipo (produto/servico): ")
        preco = input("Preço: ")
        quantidade = input("Quantidade: ")
        writer.writerow([id, nome, tipo, preco, quantidade])
        print("Produto/Serviço cadastrado.")

def listar_produtos(produtos):
    for p in produtos:
        print(p)

def buscar_produto(produtos):
    termo = input("Buscar por nome ou ID: ").lower()
    for p in produtos:
        if termo in p['nome'].lower() or termo == p['id']:
            print(p)

def ordenar_por_nome(produtos):
    ordenados = sorted(produtos, key=lambda x: x['nome'])
    listar_produtos(ordenados)

def ordenar_por_preco(produtos):
    ordenados = sorted(produtos, key=lambda x: x['preco'])
    listar_produtos(ordenados)

def atualizar_produto(produtos):
    id_alvo = input("ID do produto/serviço a atualizar: ")
    for p in produtos:
        if p['id'] == id_alvo:
            p['preco'] = float(input("Novo preço: "))
            p['quantidade'] = int(input("Nova quantidade: "))
            break
    with open('produtos.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for p in produtos:
            writer.writerow([p['id'], p['nome'], p['tipo'], p['preco'], p['quantidade']])
    print("Produto/Serviço atualizado.")

def remover_produto(produtos):
    id_alvo = input("ID do produto/serviço a remover: ")
    produtos = [p for p in produtos if p['id'] != id_alvo]
    with open('produtos.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for p in produtos:
            writer.writerow([p['id'], p['nome'], p['tipo'], p['preco'], p['quantidade']])
    print("Produto/Serviço removido.")
    return produtos

# Menu principal
def menu(usuario):
    produtos = carregar_produtos()
    while True:
        print(f"\nBem-vindo, {usuario['nome']} ({usuario['categoria']})")
        if usuario['categoria'] == 'gerente':
            print("1. Cadastrar usuário\n2. Listar usuários\n3. Atualizar usuário\n4. Remover usuário")
            print("5. Cadastrar produto\n6. Listar produtos\n7. Buscar produto\n8. Ordenar por nome\n9. Ordenar por preço")
            print("10. Atualizar produto\n11. Remover produto\n0. Sair")
        elif usuario['categoria'] == 'funcionario':
            print("5. Cadastrar produto\n6. Listar produtos\n7. Buscar produto\n0. Sair")
        elif usuario['categoria'] in ['estagiario', 'cliente']:
            print("6. Listar produtos\n7. Buscar produto\n0. Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == '1' and usuario['categoria'] == 'gerente':
            cadastrar_usuario()
        elif opcao == '2' and usuario['categoria'] == 'gerente':
            listar_usuarios()
        elif opcao == '3' and usuario['categoria'] == 'gerente':
            atualizar_usuario()
        elif opcao == '4' and usuario['categoria'] == 'gerente':
            remover_usuario()
        elif opcao == '5' and usuario['categoria'] in ['gerente', 'funcionario']:
            cadastrar_produto()
        elif opcao == '6':
            listar_produtos(produtos)
        elif opcao == '7':
            buscar_produto(produtos)
        elif opcao == '8' and usuario['categoria'] == 'gerente':
            ordenar_por_nome(produtos)
        elif opcao == '9' and usuario['categoria'] == 'gerente':
            ordenar_por_preco(produtos)
        elif opcao == '10' and usuario['categoria'] == 'gerente':
            atualizar_produto(produtos)
        elif opcao == '11' and usuario['categoria'] == 'gerente':
            produtos = remover_produto(produtos)
        elif opcao == '0':
            break
        else:
            print("Opção inválida ou sem permissão.")

# Execução
usuarios = carregar_usuarios()
usuario_logado = login(usuarios)
if usuario_logado:
    menu(usuario_logado)
