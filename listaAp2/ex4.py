def verificar_par(numero):

    if numero % 2 == 0:
        return True
    else:
        return False


numero_escolhido = int(input("Digite um número para verificar se é par ou ímpar: "))
verificar_par(numero_escolhido)
