litros = float(input("Digite o número de litros vendidos: "))
tipo = input("Digite o tipo de combustível (A-álcool, G-gasolina): ")

preco_gasolina = 2.50
preco_alcool = 1.90
valor_pagar = 0

if tipo == "A" or tipo == "a":
    if litros <= 20:
        desconto = 0.03
    else:
        desconto = 0.05
    
    valor_total = litros * preco_alcool
    valor_pagar = valor_total - (valor_total * desconto)
    print(f"Valor a pagar pelo Álcool: R$ {valor_pagar}")

elif tipo == "G" or tipo == "g":
    if litros <= 20:
        desconto = 0.04
    else:
        desconto = 0.06
        
    valor_total = litros * preco_gasolina
    valor_pagar = valor_total - (valor_total * desconto)
    print(f"Valor a pagar pela Gasolina: R$ {valor_pagar}")

else:
    print("Tipo de combustível inválido.")
