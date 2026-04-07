valor_hora = float(input("Digite o valor da sua hora: "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mes: "))

salario_bruto = valor_hora * horas_trabalhadas

if salario_bruto <= 900:
    percentual_ir = 0
elif salario_bruto <= 1500:
    percentual_ir = 5
elif salario_bruto <= 2500:
    percentual_ir = 10
else:
    percentual_ir = 20

desconto_ir = salario_bruto * (percentual_ir / 100)
desconto_inss = salario_bruto * 0.10
fgts = salario_bruto * 0.11

total_descontos = desconto_ir + desconto_inss
salario_liquido = salario_bruto - total_descontos

print(f"Salário Bruto: ({valor_hora} * {horas_trabalhadas}) : R${salario_bruto}")
print(f"(-) IR ({percentual_ir}%) : R${desconto_ir}")
print(f"(-) INSS (10%) : R${desconto_inss}")
print(f"FGTS (11%) : R${fgts}")
print(f"Total de descontos : R${total_descontos}")
print(f"Salário Liquido : R${salario_liquido}")
