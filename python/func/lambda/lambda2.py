somar = lambda x, y: x + y
resultado = somar(2, 4)
print(resultado)


lista = [2, 4, 5, 11, 8]
resultado2 = list(filter(lambda x: x % 2 == 0, lista))
print(list(resultado2))

lista3 = [(1, 2), (3, 1), (5, 6), (7, 4)]

ordenado = sorted(lista3, key= lambda x: x[1])
print(ordenado)

#


def soma(x, y):
    return x + y


def executa(f, x):
     def interna(y):
         return f(x, y)
     return interna


somando = executa(soma, 2)
print(somando(4))


