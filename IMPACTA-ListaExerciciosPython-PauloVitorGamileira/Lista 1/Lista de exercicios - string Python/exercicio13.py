palavra_secreta = "algoritmo"

palavra_embaralhada = ""

for i in range(0, len(palavra_secreta), 2):
    palavra_embaralhada = palavra_embaralhada + palavra_secreta[i]

for i in range(1, len(palavra_secreta), 2):
    palavra_embaralhada = palavra_embaralhada + palavra_secreta[i]

print("Adivinhe que palavra é esta:", palavra_embaralhada)

chute = ""
tentativas = 0
max_tentativas = 6

while chute != palavra_secreta and tentativas < max_tentativas:
    chute = input("Qual é a palavra? (Tudo minusculo): ")
    tentativas = tentativas + 1
    
    if chute == palavra_secreta:
        print("Parabéns! Você acertou!")
    else:
        if tentativas < max_tentativas:
            print("Errou! Tente novamente.")
        
if chute != palavra_secreta:
    print("Você perdeu. O número de tentativas acabou. A palavra era:", palavra_secreta)
