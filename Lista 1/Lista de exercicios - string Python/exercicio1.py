n1 = input("Digite o primeiro valor: ")
n2 = input("Digite o segundo valor: ")
print(f"Os valores são: {n1}, {n2}")

quantidade_letras1 = len(n1)
quantidade_letras2 = len(n2)
print(f"A quantidade de caracteres do primeiro valor é: {quantidade_letras1}")
print(f"A quantidade de caracteres do segundo valor é: {quantidade_letras2}")
if len(n1) == len(n2):
    print(f"Possuem o mesmo tamanho: {len(n1)} e {len(n2)}")
else: 
    print(f"Não possuem o mesmo tamanho: {len(n1)} e {len(n2)}")
if n1 == n2:
    print(f"Possuem o mesmo conteúdo: {n1} e {n2}")
else: 
    print(f"Não possuem o mesmo conteúdo: {n1} e {n2}")
