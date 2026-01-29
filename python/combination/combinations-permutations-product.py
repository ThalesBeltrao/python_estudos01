#Combinations, Permutations e product - Itertools
#combinação - Ordem não importa - iteráel + tamanho do grupo
#Produto - ordem importa e repete valores

from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep="\n")

from itertools import combinations


pessoas = ["João", "Roberto", "Thales", "Allan"]
camisetas = [
    [ "Branca"],
    ["p", "m", "g"],
    ["masculino", "feminino", "masculino"]

]

print(*list(combinations(pessoas, 2)), sep="\n")
print()
print_iter(permutations(pessoas, 2))
print()

print_iter(product(*camisetas))

for i in camisetas:
    ...

