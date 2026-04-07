valor_hora = float(input("Quanto voce ganha por hora? "))
horas_trabalhadas = float(input("Qual o numero de horas trabalhadas no mes? "))

salario_bruto = valor_hora * horas_trabalhadas
imposto_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

total_descontos = imposto_renda + inss + sindicato
salario_liquido = salario_bruto - total_descontos

print(f"+ Salário Bruto : R${salario_bruto}")
print(f"- IR (11%) : R${imposto_renda}")
print(f"- INSS (8%) : R${inss}")
print(f"- Sindicato ( 5%) : R${sindicato}")
print(f"= Salário Liquido : R${salario_liquido}")
