lista = ["a", 1, 1.1, True, [0, 1, 2], (1, 2),
         {5, 10}, {"Nome": "Luiz"}]


# tenta deixar uma lista com os mesmos elementos

# aqui voce pode saber se ele é um não de algum tipo

for item in lista:
    if isinstance(item, set):
        item.add(15)
    print(item, isinstance(item, set))

    if isinstance(item, str):

        print(item.upper(), isinstance(item, str))

    if isinstance(item, (int, float)): # voce pode passsr uma tupla
        ...