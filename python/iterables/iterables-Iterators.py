import sys
# Generator expression, iterables e Iterators

iterable = ["Eu","tenho", "__iter"]
iterator = iterable.__iter__()
print(next(iterator))
print(next(iterator))
print(next(iterator))

generator = [n for n in range(10000)] # quando se tem uma lista e se faz uma list comprehension ele guarda os valores na memoria
print(generator)                   # o problema é se sua lista for muito grande ai ele iria carregar de mais sua memoria
                                    # o generator ele faz com () como se fosse uma tuple de list comprehension nesse caso
print()
# fazendo um generator

generator2 = (n for n in range(10000))
print(generator2)

print(sys.getsizeof(generator)) # tamanho dos arquivos
print(sys.getsizeof(generator2)) # tamanho dos arquivos
print()

print(next(generator2))
print(next(generator2))
print(next(generator2))
print(next(generator2))
print(next(generator2))
print(next(generator2))

for valor in generator2:
    print(valor)

    # lista como esta salvo na memoria voce consegue acessar o indice acaba ficando mais facil para buscar valores
    # interator ele não grava tudo na memoria chama apenas um elemento por vez problemas como não salva na memoria não tem indice
    
