texto = input("Digite um texto para converter em Leet Speak: ")

texto_leet = ""

for letra in texto:
    if letra == "A" or letra == "a":
        texto_leet = texto_leet + "4"
    elif letra == "E" or letra == "e":
        texto_leet = texto_leet + "3"
    elif letra == "I" or letra == "i":
        texto_leet = texto_leet + "1"
    elif letra == "O" or letra == "o":
        texto_leet = texto_leet + "0"
    elif letra == "S" or letra == "s":
        texto_leet = texto_leet + "5"
    elif letra == "T" or letra == "t":
        texto_leet = texto_leet + "7"
    else:
        texto_leet = texto_leet + letra

print("Texto no formato leet speak:")
print(texto_leet)
