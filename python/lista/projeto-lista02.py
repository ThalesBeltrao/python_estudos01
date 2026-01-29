# Melhorar o projeto Menu  que esta bem lixo


menu = {"nome": input("Digite seu Nome: "),
            "Idade": input("Digite sua Idade: "),
        "Altura": input("Digite sua Altura: ")}


def menu1(dados):
    lista = []
    for i, k in dados.items():
        lista.append(k)
    print(lista)



menu1(menu)