# Count é um contador infinito em python
# Parecido com Range, porem ele tem início e fim e PA

from itertools import count

#Iteravel sem fim
# Precisa chamar o next
c1 = count()
r1 = range(10)


# Checarem para ver se ele é um iterável
print("c1", hasattr(c1, "__iter__"))
# E também um interator porque ele tem o método next
print("c1", hasattr(c1, "__next__"))
print()
# Analisando o Range

# Ele é um iterável porque tem o método iter
print("f1", hasattr(r1, "__iter__"))

# Ele não é um iterator por que ele não tem o método next
print("f1", hasattr(r1, "--next__"))

# Count ele não tem fim
# Por isso colocar um delimitar como um condicional
print("Count")
for i in c1:
    if i > 10:
        break
    #print(i)

print()


# Já o range ele tem como base ínicio, meio, e PA
print("Range")
for i in range(10):
    ...

    #print(i)



# No count você pode passar também uma PA
# Pode passar argumentos nomeados start, step

c2 = count(start=8, step=8)

for k in c2:
    if k > 100:
        break
    print(k)