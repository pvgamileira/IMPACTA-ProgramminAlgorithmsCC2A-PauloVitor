telefone = input("Digite o número do telefone com 7 ou 8 digitos (ex: 461-0133): ")

telefone_limpo = ""
for caracter in telefone:
    if caracter != "-":
        telefone_limpo = telefone_limpo + caracter

if len(telefone_limpo) == 7:
    print("Telefone possui 7 dígitos. Vou acrescentar o dígito '3' na frente.")
    novo_telefone = "3" + telefone_limpo
elif len(telefone_limpo) == 8:
    novo_telefone = telefone_limpo
else:
    print("Tamanho de telefone inválido. Vou usar como você digitou.")
    novo_telefone = telefone_limpo

if len(novo_telefone) == 8:
    telefone_formatado = novo_telefone[0:4] + "-" + novo_telefone[4:8]
    print("Telefone corrigido sem formatação:", novo_telefone)
    print("Telefone corrigido com formatação:", telefone_formatado)
else:
    print("Telefone final:", novo_telefone)
