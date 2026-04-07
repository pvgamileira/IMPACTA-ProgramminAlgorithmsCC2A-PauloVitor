numero = float(input("Digite um numero: "))

arredondado = round(numero)

if numero == arredondado:
    print(f"O numero {numero} e inteiro.")
else:
    print(f"O numero {numero} e decimal.")
