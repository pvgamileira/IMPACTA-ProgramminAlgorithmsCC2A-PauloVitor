def configurar_perfil(nome, idade, cidade="Desconhecida"):
    perfil = {"nome": nome, "idade": idade, "cidade": cidade}
    return perfil


nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

perfil_usuario = configurar_perfil(nome, idade, cidade)
print("Perfil do usuário:")
