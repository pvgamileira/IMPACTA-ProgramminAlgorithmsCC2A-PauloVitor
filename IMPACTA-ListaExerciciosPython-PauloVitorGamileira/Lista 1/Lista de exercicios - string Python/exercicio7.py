frase = input("Digite uma frase: ")

espacos = 0
vogais = 0

for letra in frase:
    if letra == " ":
        espacos = espacos + 1
    elif letra == "a" or letra == "A":
        vogais = vogais + 1
    elif letra == "e" or letra == "E":
        vogais = vogais + 1
    elif letra == "i" or letra == "I":
        vogais = vogais + 1
    elif letra == "o" or letra == "O":
        vogais = vogais + 1
    elif letra == "u" or letra == "U":
        vogais = vogais + 1

print("Quantidade de espaços:", espacos)
print("Quantidade de vogais:", vogais)
