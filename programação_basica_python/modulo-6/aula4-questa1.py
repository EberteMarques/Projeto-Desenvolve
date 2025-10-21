numeros_pares = [num for num in range(20, 51, 2)]
print(f"Números pares entre 20 e 50: {numeros_pares}")

lista_valores_originais = [3-11]
quadrados = [num**2 for num in lista_valores_originais]
print(f"Quadrados dos valores: {quadrados}")

divisiveis_por_7 = [num for num in range(1, 101) if num % 7 == 0]
print(f"Números entre 1 e 100 divisíveis por 7: {divisiveis_por_7}")

paridade_elementos = ["par" if num % 2 == 0 else "ímpar" for num in range(0, 30, 3)]
print(f"Paridade dos elementos em range(0,30,3): {paridade_elementos}")