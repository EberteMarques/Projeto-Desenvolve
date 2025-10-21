def validador_senha(senha):
  """
  Verifica se uma senha atende aos critérios de segurança:
  - Pelo menos 8 caracteres de comprimento.
  - Pelo menos uma letra maiúscula.
  - Pelo menos uma letra minúscula.
  - Pelo menos um número.
  - Pelo menos um caractere especial.
  Retorna True se todos os critérios forem atendidos, False caso contrário.
  """
  # Inicializa as variáveis de controle
  tem_maiuscula = False
  tem_minuscula = False
  tem_numero = False
  tem_especial = False
  
  # Critério 1: Verifica o comprimento da senha
  if len(senha) < 8:
    return False

  # Itera sobre cada caractere da senha
  for caractere in senha:
    if caractere.isupper():
      tem_maiuscula = True
    elif caractere.islower():
      tem_minuscula = True
    elif caractere.isdigit():
      tem_numero = True
    # Se não for maiúscula, minúscula ou número, é considerado especial.
    elif not caractere.isalnum():
      tem_especial = True
  
  # Retorna True apenas se todos os critérios forem atendidos
  return tem_maiuscula and tem_minuscula and tem_numero and tem_especial

senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "Senha_fraca"
senha4 = "12345678"
print(f'"{senha1}" é válida? {validador_senha(senha1)}')  # Saída esperada: True
print(f'"{senha2}" é válida? {validador_senha(senha2)}')  # Saída esperada: False
print(f'"{senha3}" é válida? {validador_senha(senha3)}')  # Saída esperada: False
print(f'"{senha4}" é válida? {validador_senha(senha4)}')  # Saída esperada: False