texto = input("Digite uma palavra ou frase: ")

# Limpando a string tirando apenas espaços para simplificar
texto_limpo = ""
for letra in texto:
    if letra != " ":
        texto_limpo = texto_limpo + letra.upper()

texto_invertido = ""
# invertendo a string do final pro começo
for i in range(len(texto_limpo) - 1, -1, -1):
    texto_invertido = texto_invertido + texto_limpo[i]

if texto_limpo == texto_invertido:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
