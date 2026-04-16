nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 9.0 and media <= 10.0:
    conceito = "A"
elif media >= 7.5 and media < 9.0:
    conceito = "B"
elif media >= 6.0 and media < 7.5:
    conceito = "C"
elif media >= 4.0 and media < 6.0:
    conceito = "D"
else:
    conceito = "E"

if conceito == "A" or conceito == "B" or conceito == "C":
    mensagem = "APROVADO"
else:
    mensagem = "REPROVADO"

print(f"Notas: {nota1} e {nota2}")
print(f"Média: {media}")
print(f"Conceito: {conceito}")
print(mensagem)
