tipo_carne = input("Digite o tipo da carne (F para File Duplo, A para Alcatra, P para Picanha): ")
quantidade_carne = float(input("Digite a quantidade de carne em Kg: "))
cartao_tabajara = input("A compra será feita no cartão Tabajara? (S - Sim, N - Não): ")

preco_kg = 0
nome_carne = ""
tipo_pagamento = "Dinheiro / Outro Cartão"

if tipo_carne == "F" or tipo_carne == "f":
    nome_carne = "File Duplo"
    if quantidade_carne <= 5:
        preco_kg = 4.90
    else:
        preco_kg = 5.80
elif tipo_carne == "A" or tipo_carne == "a":
    nome_carne = "Alcatra"
    if quantidade_carne <= 5:
        preco_kg = 5.90
    else:
        preco_kg = 6.80
elif tipo_carne == "P" or tipo_carne == "p":
    nome_carne = "Picanha"
    if quantidade_carne <= 5:
        preco_kg = 6.90
    else:
        preco_kg = 7.80
else:
    print("Tipo de carne inválido.")
    preco_kg = -1

if preco_kg != -1:
    preco_total = quantidade_carne * preco_kg
    desconto = 0

    if cartao_tabajara == "S" or cartao_tabajara == "s":
        desconto = preco_total * 0.05
        tipo_pagamento = "Cartão Tabajara"

    valor_pagar = preco_total - desconto

    print("--- CUPOM FISCAL ---")
    print(f"Tipo de carne: {nome_carne}")
    print(f"Quantidade: {quantidade_carne} Kg")
    print(f"Preço Total: R$ {preco_total}")
    print(f"Tipo de Pagamento: {tipo_pagamento}")
    print(f"Valor do Desconto: R$ {desconto}")
    print(f"Valor a Pagar: R$ {valor_pagar}")
