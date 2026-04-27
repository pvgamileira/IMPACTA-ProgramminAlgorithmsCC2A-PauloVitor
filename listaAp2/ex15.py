def produtoMaisCaro(produtos):
    Mais_Caro = produtos[0]
    for produto in produtos:
        if produto["preco"] > Mais_Caro["preco"]:
            Mais_Caro = produto
    return Mais_Caro["nome"]


produtos = [
    {
        "nome": "Arroz e Feijão (Opcional) com Filé de Frango Empanado Salada e Fritas",
        "preco": 23.90,
    },
    {
        "nome": "Arroz e Feijão (Opcional) com Filé de Frango Protéico Salada e Fritas",
        "preco": 19.90,
    },
    {
        "nome": "Arroz e Feijão (Opcional) com Filé de Merluza Salada e Fritas",
        "preco": 28.90,
    },
    {
        "nome": "Macarrão e Frango a Milanesa com Salada e/ou Fritas (Opcional)",
        "preco": 24.90,
    },
]


resultado = produtoMaisCaro(produtos[0:4])
print(f"O produto mais caro é: {resultado}")
