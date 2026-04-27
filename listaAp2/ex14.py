nickname = input("Digite seu nickname: ")


def create_character(nickname):
    nickname = input("Digite outro nickname nesse campo: ")
    print(f"O usuário escolhido foi {nickname} ?")
    return nickname


create_character(nickname)

print(f"Ou seu usuário escolhido foi {nickname}?")
