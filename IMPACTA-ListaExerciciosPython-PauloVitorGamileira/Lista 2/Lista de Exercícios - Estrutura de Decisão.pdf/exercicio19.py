numero = int(input("Digite um numero inteiro menor que 1000: "))

if numero >= 1000 or numero < 0:
    print("Numero invalido.")
else:
    centenas = numero // 100
    resto = numero % 100
    dezenas = resto // 10
    unidades = resto % 10

    resultado = ""

    if centenas > 0:
        if centenas == 1:
            resultado = resultado + "1 centena"
        else:
            resultado = resultado + str(centenas) + " centenas"

    if dezenas > 0:
        if centenas > 0 and unidades > 0:
            resultado = resultado + ", "
        elif centenas > 0 and unidades == 0:
            resultado = resultado + " e "
        
        if dezenas == 1:
            resultado = resultado + "1 dezena"
        else:
            resultado = resultado + str(dezenas) + " dezenas"

    if unidades > 0:
        if centenas > 0 or dezenas > 0:
            resultado = resultado + " e "
            
        if unidades == 1:
            resultado = resultado + "1 unidade"
        else:
            resultado = resultado + str(unidades) + " unidades"

    if numero == 0:
        resultado = "0 unidades"

    print(f"{numero} = {resultado}")
