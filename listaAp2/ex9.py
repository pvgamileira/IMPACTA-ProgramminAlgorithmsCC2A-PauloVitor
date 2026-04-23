def fatorial_iterativo(n):
    resultado = 1
    for numero in range(1, n + 1):
        resultado *= numero  # Multiplica o resultado atual pelo próximo número
    return resultado


n1 = input("Digite um número para calcular o fatorial: ")
print(fatorial_iterativo(int(n1)))  # Exemplo de uso, deve imprimir 120
