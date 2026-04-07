numero_str = input("Digite um número até 99: ")
numero = int(numero_str)

unidades = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
especiais = ["dez", "onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
dezenas = ["", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]

if numero < 10:
    print(unidades[numero])
elif numero >= 10 and numero < 20:
    # Aqui a gente diminui 10 para pegar o índice certo na lista especiais
    print(especiais[numero - 10])
else:
    # Se o número for de 20 para cima
    dezena_str = numero_str[0]
    unidade_str = numero_str[1]
    
    dezena_int = int(dezena_str)
    unidade_int = int(unidade_str)
    
    if unidade_int == 0:
        print(dezenas[dezena_int])
    else:
        print(dezenas[dezena_int] + " e " + unidades[unidade_int])
