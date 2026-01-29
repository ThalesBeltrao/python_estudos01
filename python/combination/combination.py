# Combination, Permutation e product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - ordem importa
# Produto - Ordem importa e repete valores únicos


from itertools import combinations, permutations, product

pessoas = [
    "Thales", "Natasha", "Sabrina"
]


camisetas = [
    ["preta", " Branca"], ["p", "m", "g"], ["masculino", "feminino"],
]

# Combination não repete valores,
#print(*combinations(pessoas, 2), sep="\n")
#('Thales', 'Natasha')
#('Thales', 'Sabrina')
#('Natasha', 'Sabrina')
# print()

# Permutação a ordem importa, então repete valores
# print(*permutations(pessoas, 2), sep="\n")

#('Thales', 'Natasha')
#('Thales', 'Sabrina')
#('Natasha', 'Thales')
#('Natasha', 'Sabrina')
#('Sabrina', 'Thales')
#('Sabrina', 'Natasha')
#print()
#print("Product")

# O produto ele cresce de maneira exponêncial

#produto = list(product(*camisetas))

#or i in produto:
    #print(i)