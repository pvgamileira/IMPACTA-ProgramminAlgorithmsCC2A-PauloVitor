# Exercício 2: Cálculo de Imposto (Funções com Retorno)
# Objetivo: Praticar funções que realizam cálculos matemáticos e retornam
# resultados para o programa principal.
# Enunciado: Crie uma função chamada soma_imposto que possua dois
# parâmetros:
# 1. taxa_imposto: a quantia de imposto sobre vendas expressa em
# porcentagem (ex: 10 para 10%).
# 2. custo: o valor de um item antes do imposto.
# A função deve calcular o valor final do produto (custo + imposto) e retornar esse
# novo valor. Em seguida, peça ao usuário que digite o custo e a taxa, chame a
# função e imprima o resultado com duas casas decimais.

# Dica para resolver:
# • Use o return quando precisar que o resultado da função seja guardado em
# uma variável ou usado em um cálculo posterior.
# • Lembre-se de definir a função com def antes de tentar chamá-la no seu
# código.



def soma_imposto(taxa_imposto, custo_item):
    calculo_imposto = custo_item * (taxa_imposto / 100)
    valor_final = calculo_imposto + custo_item
    return valor_final



custo_item = float(input("Digite o custo do produto: R$"))
taxa_imposto = float(input("Digite a taxa de imposto do produto: R$"))   

resultado = soma_imposto(taxa_imposto,custo_item)

print(f"Sua soma de imposto é: R${resultado:.2f}")