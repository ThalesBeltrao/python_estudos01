#count iterador sem fim ele esta no metodo itertools
from itertools import count

c1 = count() # interator que não tem fim ele tem inicio e pular
c2 = range(1)
for i in c1:
    if i > 100:
        break
    print(i)

print()

for i in range(1,100):
    print(i)
