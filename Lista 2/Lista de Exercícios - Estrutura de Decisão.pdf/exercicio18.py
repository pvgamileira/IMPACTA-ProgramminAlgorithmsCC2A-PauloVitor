data = input("Digite uma data no formato dd/mm/aaaa: ")

dia_str = ""
mes_str = ""
ano_str = ""
parte = 1

for char in data:
    if char == "/":
        parte = parte + 1
    elif parte == 1:
        dia_str = dia_str + char
    elif parte == 2:
        mes_str = mes_str + char
    elif parte == 3:
        ano_str = ano_str + char

if dia_str == "" or mes_str == "" or ano_str == "":
    print("Formato inválido.")
else:
    dia = int(dia_str)
    mes = int(mes_str)
    ano = int(ano_str)

    data_valida = True

    if mes < 1 or mes > 12:
        data_valida = False
    elif dia < 1 or dia > 31:
        data_valida = False
    else:
        if (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30:
            data_valida = False
        elif mes == 2:
            bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
            if bissexto and dia > 29:
                data_valida = False
            elif not bissexto and dia > 28:
                data_valida = False

    if data_valida:
        print(f"A data {data} é válida.")
    else:
        print(f"A data {data} é inválida.")
