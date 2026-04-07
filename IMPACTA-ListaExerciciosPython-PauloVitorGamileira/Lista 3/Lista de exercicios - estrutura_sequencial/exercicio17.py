area = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))

area_com_folga = area * 1.1

cobertura_lata = 18 * 6  # 108 m2
preco_lata = 80.0

cobertura_galao = 3.6 * 6  # 21.6 m2
preco_galao = 25.0

print("Situação 1: Comprar apenas latas de 18 litros")
latas_apenas = int(area_com_folga / cobertura_lata)
if area_com_folga % cobertura_lata != 0:
    latas_apenas = latas_apenas + 1
valor_apenas_latas = latas_apenas * preco_lata
print(f"Latas necessárias: {latas_apenas}. Valor: R${valor_apenas_latas}")

print("Situação 2: Comprar apenas galões de 3,6 litros")
galoes_apenas = int(area_com_folga / cobertura_galao)
if area_com_folga % cobertura_galao != 0:
    galoes_apenas = galoes_apenas + 1
valor_apenas_galoes = galoes_apenas * preco_galao
print(f"Galões necessários: {galoes_apenas}. Valor: R${valor_apenas_galoes}")

print("Situação 3: Misturar latas e galões para menor preço")
latas_mistura = int(area_com_folga / cobertura_lata)
area_restante = area_com_folga - (latas_mistura * cobertura_lata)

galoes_mistura = int(area_restante / cobertura_galao)
if area_restante % cobertura_galao != 0:
    galoes_mistura = galoes_mistura + 1

if (galoes_mistura * preco_galao) > preco_lata:
    latas_mistura = latas_mistura + 1
    galoes_mistura = 0

valor_mistura = (latas_mistura * preco_lata) + (galoes_mistura * preco_galao)

print(f"Mistura ideal: {latas_mistura} latas e {galoes_mistura} galões. Valor: R${valor_mistura}")
