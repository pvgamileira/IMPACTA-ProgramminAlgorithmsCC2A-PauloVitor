num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
operacao = input("Digite a operacao desejada (+, -, *, /): ")

resultado = 0
operacao_valida = True

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Erro: Divisao por zero.")
        operacao_valida = False
else:
    print("Operacao invalida.")
    operacao_valida = False

if operacao_valida:
    print(f"Resultado da operacao: {resultado}")
    
    if resultado == round(resultado):
        if resultado % 2 == 0:
            print("O resultado é par.")
        else:
            print("O resultado é impar.")
    else:
        print("O resultado nao é par nem impar pois é decimal.")
    
    if resultado > 0:
        print("O resultado é positivo.")
    elif resultado < 0:
        print("O resultado é negativo.")
    else:
        print("O resultado é zero.")
        
    if resultado == round(resultado):
        print("O resultado é inteiro.")
    else:
        print("O resultado é decimal.")
