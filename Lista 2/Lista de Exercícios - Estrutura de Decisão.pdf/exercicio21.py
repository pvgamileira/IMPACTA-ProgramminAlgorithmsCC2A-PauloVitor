saque = int(input("Digite o valor que deseja sacar (entre 10 e 600): "))

if saque < 10 or saque > 600:
    print("Valor invalido para saque. O minimo e 10 e o maximo e 600.")
else:
    notas_100 = saque // 100
    resto = saque % 100

    notas_50 = resto // 50
    resto = resto % 50

    notas_10 = resto // 10
    resto = resto % 10

    notas_5 = resto // 5
    resto = resto % 5

    notas_1 = resto

    print(f"Para sacar a quantia de {saque} reais, o programa fornece:")
    if notas_100 > 0:
        print(f"{notas_100} nota(s) de 100")
    if notas_50 > 0:
        print(f"{notas_50} nota(s) de 50")
    if notas_10 > 0:
        print(f"{notas_10} nota(s) de 10")
    if notas_5 > 0:
        print(f"{notas_5} nota(s) de 5")
    if notas_1 > 0:
        print(f"{notas_1} nota(s) de 1")
