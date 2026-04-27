def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        resultado = fib(n - 1) + fib(n - 2)
        return resultado


numero = int(input("Digite um número inteiro: "))
print(f"{fib(numero)}")
