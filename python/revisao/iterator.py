import sys
# generator são funções que sabe pausar em determinadas ocasiões

iterable = ["Eu", "Tenho", "_iter_"]
iterator = iter(iterable)

# generator pega um valor por vez em vez de salvar
# todos os dados na memória

# ela compacta os dados deixando o valor menor que uma lista por exemplo com o mesmo valor
# voce consegue colocar o valor que for que ele ficará no mesmo padrão

generator = (n for n in range(100000))
print(f" Vaor do Generator em Bytes: {sys.getsizeof(generator)}")

print()

# fazendo o comparativo com a lista por exemplo

lista = [n for n in range(100000)]
print(f" Vaor da Lista em Bytes: {sys.getsizeof(lista)}")

# para chamar o generation ele chama com next
# generation não tem tamanho nem indice é penas para ocupar menos espaço
print(next(generator))
print(next(generator))
print()
# posso chamar ele de uma vez com o for

# function generation


def generator(n=0):
    yield 1
    print("Continuando...")
    yield 2
    print("Mais uma...")
    yield 3
    print("Vou terminar")
    return "ACABOU"


gen = generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))


# Como fazer de maneira interativa

#for n in gen:
    #print(n)



# criando uma funcao geradora
# voce basicamente cria um range


def generator1(n=0, maximum=10):
    while True:
        yield n
        n += 1
        if n > maximum:
            return


# gen10 = generator1(5, 10)

# for n in gen10:
    # print(n)


# yield from ele pega outra parte do seu contigo e continua


def contar_1():
    yield 1
    yield 2
    yield 3


def continuar():

    yield from contar_1()
    yield 4
    yield 5
    yield 6


for i in continuar():
    print(i)