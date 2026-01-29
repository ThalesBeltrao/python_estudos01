# isinstance para saber se objeto é de que tip

lista = [
    "a",1,1,1,True, [0,1,2], (1,2),
    {0,1}, {"nome": "luiz"},

]
for item in lista:
    print(item, isinstance(item, set)) # é instancia DE nesse caso o isinstance  ele vai interar sobre cada item da lista o instance serve ver qual tipo de classe é os valores da lista
    if isinstance(item, set):
        item.add(5)
        print(lista[7])

    if isinstance(item, str):
        item.upper()
        print(lista[8])

    if isinstance(item, dict):
        ...


print()



print(lista)

