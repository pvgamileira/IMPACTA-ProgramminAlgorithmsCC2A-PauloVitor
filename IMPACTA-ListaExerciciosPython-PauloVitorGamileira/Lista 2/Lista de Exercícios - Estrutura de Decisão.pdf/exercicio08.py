preco1 = float(input("Digite o preco do produto 1: "))
preco2 = float(input("Digite o preco do produto 2: "))
preco3 = float(input("Digite o preco do produto 3: "))

if preco1 <= preco2 and preco1 <= preco3:
    print(f"Voce deve comprar o produto 1, que custa {preco1}")
elif preco2 <= preco1 and preco2 <= preco3:
    print(f"Voce deve comprar o produto 2, que custa {preco2}")
else:
    print(f"Voce deve comprar o produto 3, que custa {preco3}")
