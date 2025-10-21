horas_trabalhadas = [3, 3, 3-6]
ganho_por_hora = 20
hora_extra = 25

pagamentos = [ganho_por_hora * min(hora, 40) + hora_extra * max(0, hora-40) for hora in horas_trabalhadas]
print(pagamentos)