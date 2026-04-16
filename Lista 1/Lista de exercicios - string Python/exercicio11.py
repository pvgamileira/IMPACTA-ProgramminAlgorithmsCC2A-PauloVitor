import random

palavras = ["banana", "abacate", "computador", "teclado", "cachorro"]

# Pegar uma palavra aleatória (de forma literal)
indice = random.randint(0, len(palavras) - 1)
palavra_secreta = palavras[indice]

letras_descobertas = []
for i in range(len(palavra_secreta)):
    letras_descobertas.append("_")

erros = 0
max_erros = 6
acertou_tudo = False

print("Bem-vindo ao Jogo da Forca!")

while erros < max_erros and acertou_tudo == False:
    # Mostrar como está a palavra
    palavra_mostrar = ""
    for letra in letras_descobertas:
        palavra_mostrar = palavra_mostrar + letra + " "
    print("Palavra:", palavra_mostrar)
    print("Erros:", erros, "/", max_erros)
    
    chute = input("Digite uma letra: ")
    
    acertou_letra = False
    for i in range(len(palavra_secreta)):
        if chute == palavra_secreta[i]:
            letras_descobertas[i] = chute
            acertou_letra = True
            
    if acertou_letra == False:
        erros = erros + 1
        print("Você errou!")
    else:
        print("Você acertou a letra!")
        
    # Verificar se já ganhou (se não tem mais underline)
    tem_sublinhado = False
    for letra in letras_descobertas:
        if letra == "_":
            tem_sublinhado = True
            
    if tem_sublinhado == False:
        acertou_tudo = True

if acertou_tudo == True:
    print("Parabéns, você ganhou! A palavra era:", palavra_secreta)
else:
    print("Você perdeu! A palavra era:", palavra_secreta)
