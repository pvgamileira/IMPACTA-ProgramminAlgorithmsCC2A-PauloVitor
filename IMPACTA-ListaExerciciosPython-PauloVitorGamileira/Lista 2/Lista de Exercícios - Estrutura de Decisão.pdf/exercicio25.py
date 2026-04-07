print("Responda as perguntas com S para Sim ou N para Não.")

perg1 = input("1. Telefonou para a vítima? ")
perg2 = input("2. Esteve no local do crime? ")
perg3 = input("3. Mora perto da vítima? ")
perg4 = input("4. Devia para a vítima? ")
perg5 = input("5. Já trabalhou com a vítima? ")

respostas_positivas = 0

if perg1 == "S" or perg1 == "s":
    respostas_positivas = respostas_positivas + 1
if perg2 == "S" or perg2 == "s":
    respostas_positivas = respostas_positivas + 1
if perg3 == "S" or perg3 == "s":
    respostas_positivas = respostas_positivas + 1
if perg4 == "S" or perg4 == "s":
    respostas_positivas = respostas_positivas + 1
if perg5 == "S" or perg5 == "s":
    respostas_positivas = respostas_positivas + 1

if respostas_positivas == 2:
    print("Classificação: Suspeita")
elif respostas_positivas == 3 or respostas_positivas == 4:
    print("Classificação: Cúmplice")
elif respostas_positivas == 5:
    print("Classificação: Assassino")
else:
    print("Classificação: Inocente")
