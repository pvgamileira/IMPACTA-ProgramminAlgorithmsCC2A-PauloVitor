cpf_formatado = input("Digite o CPF (xxx.xxx.xxx-xx): ")

# Pegar apenas os números
cpf_numeros = ""
for caracter in cpf_formatado:
    if caracter != "." and caracter != "-":
        cpf_numeros = cpf_numeros + caracter

if len(cpf_numeros) != 11:
    print("CPF inválido (O tamanho está incorreto).")
else:
    # Cálculo do primeiro dígito
    soma1 = 0
    multiplicador1 = 10
    for i in range(0, 9):
        numero = int(cpf_numeros[i])
        soma1 = soma1 + (numero * multiplicador1)
        multiplicador1 = multiplicador1 - 1
    
    resto1 = soma1 % 11
    if resto1 < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto1
        
    # Cálculo do segundo dígito
    soma2 = 0
    multiplicador2 = 11
    for i in range(0, 10):
        numero = int(cpf_numeros[i])
        soma2 = soma2 + (numero * multiplicador2)
        multiplicador2 = multiplicador2 - 1
        
    resto2 = soma2 % 11
    if resto2 < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto2
        
    # Verificar se bate com os digitos informados
    if str(digito1) == cpf_numeros[9] and str(digito2) == cpf_numeros[10]:
        print("CPF válido.")
    else:
        print("CPF inválido.")
