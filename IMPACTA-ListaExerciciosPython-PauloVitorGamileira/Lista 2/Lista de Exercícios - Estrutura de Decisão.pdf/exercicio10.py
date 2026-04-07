turno = input("Em que turno voce estuda? M - Matutino, V - Vespertino, N - Noturno: ")

if turno == "M" or turno == "m":
    print("Bom Dia!")
elif turno == "V" or turno == "v":
    print("Boa Tarde!")
elif turno == "N" or turno == "n":
    print("Boa Noite!")
else:
    print("Valor Inválido!")
