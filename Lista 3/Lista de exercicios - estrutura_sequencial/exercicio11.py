int1 = int(input("Digite o primeiro numero inteiro: "))
int2 = int(input("Digite o segundo numero inteiro: "))
real = float(input("Digite um numero real: "))

a = (2 * int1) + (int2 / 2)
b = (3 * int1) + real
c = real ** 3

print(f"O produto do dobro do primeiro com metade do segundo é: {a}")
print(f"A soma do triplo do primeiro com o terceiro é: {b}")
print(f"O terceiro elevado ao cubo é: {c}")
