def validar_cpf(cpf_str):
   
    # Remove pontos e traço
    cpf_limpo = cpf_str.replace('.', '').replace('-', '')

    # Verifica se o CPF tem 11 dígitos
    if len(cpf_limpo) != 11:
        return "Inválido"

    # Verifica se todos os dígitos são iguais (ex: 111.111.111-11)
    if cpf_limpo == cpf_limpo[0] * 11:
        return "Inválido"

    # Converte os dígitos para uma lista de inteiros
    cpf_numeros = [int(d) for d in cpf_limpo]

    # --- Cálculo do primeiro dígito verificador ---
    soma_primeiro_digito = 0
    multiplicador = 10
    for i in range(9):
        soma_primeiro_digito += cpf_numeros[i] * multiplicador
        multiplicador -= 1

    resto_primeiro = soma_primeiro_digito % 11
    if resto_primeiro < 2:
        digito1_calculado = 0
    else:
        digito1_calculado = 11 - resto_primeiro

    # Compara o primeiro dígito calculado com o do CPF informado
    if digito1_calculado != cpf_numeros[9]:
        return "Inválido"

    # --- Cálculo do segundo dígito verificador ---
    soma_segundo_digito = 0
    multiplicador = 11
    for i in range(10):
        soma_segundo_digito += cpf_numeros[i] * multiplicador
        multiplicador -= 1
    
    resto_segundo = soma_segundo_digito % 11
    if resto_segundo < 2:
        digito2_calculado = 0
    else:
        digito2_calculado = 11 - resto_segundo

    # Compara o segundo dígito calculado com o do CPF informado
    if digito2_calculado != cpf_numeros[10]:
        return "Inválido"

    return "Válido"

# Solicita o CPF do usuário
cpf_digitado = input("Digite um CPF (XXX.XXX.XXX-XX): ")
resultado = validar_cpf(cpf_digitado)
print(resultado)