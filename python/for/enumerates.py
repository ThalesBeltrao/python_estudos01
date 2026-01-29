lista = ["thales", "willian","Beltrao", 1]
lista2 = ["thales", "willian","Beltrao", 1, 2]
n = [10, 20, 30]

lista_enum = enumerate(lista)
#print(*lista_enum)

for k, v in lista_enum:
    print(k, v)

#for k, v in enumerate(n):
    #n[k] = v  * 10

#print(n)

# uma forma mais rapida list comprehension
#n_multi = [v * 10 for v in n ]
#print(n_multi)

for k, v in enumerate(n):
    if v > 10:
        n[k] = v * 10

print(n)

# uma forma mais rapida list comprehension
n_if_mult = [v * 10 for v in n if v >10 ]
print(n_if_mult)

# Outra forma aparecendo toda a lista deixar o for por ultimo

n2 = [v * 10 if v > 10 else v for v in n ]
print(n2)