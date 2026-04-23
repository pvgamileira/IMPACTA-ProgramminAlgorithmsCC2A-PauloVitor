# Quantidade de vogais
def contar_vogais(frase):
    vogais = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    contador = 0
    for letra in frase:
        if letra in vogais:
            contador += 1

    return contador


frase = input("Digite uma frase: ")
print(f"Sua frase tem a seguinte quantidade de vogais: {contar_vogais(frase)}")
