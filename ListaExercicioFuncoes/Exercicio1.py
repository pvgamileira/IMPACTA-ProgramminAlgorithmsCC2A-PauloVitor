# Exercício 1: Validação de Strings e Parâmetros
# Objetivo: Criar uma função que valide o tamanho de uma string, simulando uma
# consistência de dados.
# Enunciado: Escreva uma função chamada valida_string que receba três
# parâmetros: uma string, um valor mínimo e um valor máximo.
# • A função deve retornar True se o comprimento da string estiver entre o
# mínimo e o máximo (inclusive) , e False caso contrário.
# • Torne os parâmetros mínimo e máximo opcionais, com valores padrão de 1
# e 100, respectivamente.

def valida_string(string, valor_min = 1, valor_max = 100) :
    if valor_min <= len(string) <= valor_max:  
        return True 
    else:
        return False
        
    

print(valida_string(''))

