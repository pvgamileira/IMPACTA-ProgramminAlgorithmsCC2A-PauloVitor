def inverter_palavra(palavra):
    palavra_invertida = palavra[::-1]
    return palavra_invertida


digite = input("Digite uma palavra: ")
palavra_invertida = digite
print(f"Sua palavra ao contrário é: {inverter_palavra(palavra_invertida)}")
