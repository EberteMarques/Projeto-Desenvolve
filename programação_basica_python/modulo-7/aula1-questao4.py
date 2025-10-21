def formatar_numero_celular(numero):

  # Remove espaços em branco ou outros caracteres não numéricos
  numero = "".join(filter(str.isdigit, numero))

  if len(numero) == 8:
    numero_completo = '9' + numero
  elif len(numero) == 9:
    numero_completo = numero
  else:
    return "Número inválido. O número deve ter 8 ou 9 dígitos."

  # Adiciona o separador '-'
  return f"{numero_completo[:5]}-{numero_completo[5:]}"

# Exemplo de uso
numero_digitado = input("Digite o número: ")
numero_formatado = formatar_numero_celular(numero_digitado)

print(f"Número completo: {numero_formatado}")