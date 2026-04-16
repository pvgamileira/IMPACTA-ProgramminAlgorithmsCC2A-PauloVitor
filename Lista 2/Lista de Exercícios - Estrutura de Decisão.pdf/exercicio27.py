kg_morango = float(input("Digite a quantidade de morangos em Kg: "))
kg_maca = float(input("Digite a quantidade de maçãs em Kg: "))

preco_morango = 0
preco_maca = 0

if kg_morango <= 5:
    preco_morango = 2.50
else:
    preco_morango = 2.20

if kg_maca <= 5:
    preco_maca = 1.80
else:
    preco_maca = 1.50

valor_total_morango = kg_morango * preco_morango
valor_total_maca = kg_maca * preco_maca
valor_total_compra = valor_total_morango + valor_total_maca

kg_total = kg_morango + kg_maca

if kg_total > 8 or valor_total_compra > 25.00:
    desconto = valor_total_compra * 0.10
    valor_total_compra = valor_total_compra - desconto

print(f"Valor a ser pago: R$ {valor_total_compra}")
