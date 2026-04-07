peso = float(input("Digite o peso dos peixes pescados (em kg): "))

excesso = 0
multa = 0

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4.00

print(f"Peso total: {peso} kg")
print(f"Excesso de peso: {excesso} kg")
print(f"Valor da multa: R${multa}")
