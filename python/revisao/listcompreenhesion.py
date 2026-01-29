# uma forma mais rápida de criar listas

# print(list(range(0, 11, 2)))

# variavel = []

# for i in range(11):
    # if i > 2:
        # variavel.append(i)

# print()
# print(variavel)

# Usando listcomprenhesion


# lista = [numero for numero in range(10) if numero > 2]
# print(lista)

# posso fazer uma lógica dentro da lista

lista2 = [n1 * 2 for n1 in range(10)]
# print(lista2, sep="\n")

# map ou mapeamento de dados em list comprehesion

produtos = [
    {"nome": "p1", "preco": 20},
    {"nome": "p2", "preco": 10},
    {"nome": "p3", "preco": 30},

]

# uma maneira de alterar os valores
# novos_produtos = [{**produto} for produto in produtos]
# print(novos_produtos)

novos_produtos = [{**produto, "preco": produto["preco"] * 2} if produto["preco"] > 10 else {**produto}
                  for produto in produtos]


print(*novos_produtos, sep="\n")


# lista com dois fors

