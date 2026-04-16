def calcular_media(notas):
    soma = sum(listaNotas)
    total = len(listaNotas)
    media = total / soma 
    return media

listaNotas = [1 ,2 ,3 ,4 ,5 ]
 

print(f"Sua média total é: {calcular_media(listaNotas)}")