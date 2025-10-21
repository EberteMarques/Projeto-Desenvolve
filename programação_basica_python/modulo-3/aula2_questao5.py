nome = str(input("Qual é o seu nome: "))

genero = str(input("Qual o seu genero? digite 'm' para masculino ou 'f' para feminino: "))

id = int(input(f"Qual sua idade {nome}? "))

tempo = int(input("Qual é o seu tempo de serviço?: "))

a = (genero == "f" and id >= 60) or (genero == "m" and id >= 65)
b = tempo >= 30
c= id >= 60 and tempo >= 25

pode_aposentar = a or b or c

print(f"{nome}, tendo em vista que as respostas para as preguntas foram: ", a, b, c, "a informação que você já preencheu os requisitos para se aposentar é: ",pode_aposentar)