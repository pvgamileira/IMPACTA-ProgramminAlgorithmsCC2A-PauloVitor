for txt in range(0, 4):
    arquivo = open("RA.txt", "w")
    arquivo = open("RA1.txt", "w")
    arquivo = open("RA2.txt", "w")
    arquivo.write("2503481")
    if txt == arquivo:
        arquivo = open("RA.txt", "r")
        arquivo.write("1")
        print(arquivo.read())
        arquivo += 1
    elif txt != arquivo:
        arquivo = open("RA1.txt", "w")
        arquivo.write("2")
        print(arquivo.read())
        arquivo += 21
    else:
        arquivo = open("RA2.txt", "r")
        arquivo.write(+"3")
        print(arquivo.read())
        arquivo += 3
