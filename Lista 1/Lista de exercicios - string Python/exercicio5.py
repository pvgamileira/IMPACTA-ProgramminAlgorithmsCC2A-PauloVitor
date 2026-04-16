nome = input("Digite o seu nome: ")
tamanho = len(nome)

for i in range(tamanho, 0, -1):
    print(nome[0:i])
