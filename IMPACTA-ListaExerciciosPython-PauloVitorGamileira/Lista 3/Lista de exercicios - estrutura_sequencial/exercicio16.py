area = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))
cobertura_lata = 18 * 3  # 54 m2
preco_lata = 80.0

latas = int(area / cobertura_lata)
if area % cobertura_lata != 0:
    latas = latas + 1

valor_total = latas * preco_lata

print(f"Quantidade de latas a comprar: {latas}")
print(f"Preço total: R${valor_total}")
