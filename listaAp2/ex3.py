def maior_valor(a, b):
    if a > b:
        return a
    return b


a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))


print(f"O maior valor é: {maior_valor(a, b)}")
