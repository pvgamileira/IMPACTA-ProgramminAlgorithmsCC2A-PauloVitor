lado1 = float(input("Digite o primeiro lado do triangulo: "))
lado2 = float(input("Digite o segundo lado do triangulo: "))
lado3 = float(input("Digite o terceiro lado do triangulo: "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print("Os valores podem ser um triângulo.")
    if lado1 == lado2 and lado2 == lado3:
        print("Triângulo Equilátero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")
else:
    print("Os valores não formam um triângulo.")
