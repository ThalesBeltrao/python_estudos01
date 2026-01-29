from math import factorial

"""
Lambda em Python
funções anonimas que contem apenas uma linha ou seja , tudo deve ser contido dentro de uma unica expressao


lista = [4, 2, 30, 10, 1, 50, 20, 17, 5, 17, 8]
lista.sort()# ordena a lista ou melhor coloca a lista na ordem do menor para o maior
lista.reverse() # do maior para o menor
print(lista)

# ordenar dic com dic
lista1 = [
    {"nome":"carlos","sobrenome":"willian"},
    {"nome":"amanda","sobrenome":"roberto"},
    {"nome":"bruno","sobrenome":"jesus"},
    {"nome":"danil","sobrenome":"silva"}
]
def ordena(item):
    #print(item)
    return item["nome"]

#lista1.sort(key=ordena)
#usando lambda

lista1.sort(key=lambda item: item["nome"])

for i in lista1:
    print(i)


def executa(funcao, *args):  #criou uma funcao que executa uma funcao
    return funcao(*args)   #recebe uma funcao não nomeada

def soma(x, y):
    return x + y

#def cria_multiplicador(multiplicador):
   # def multiplica(numero):
       # return numero * multiplicador
    #return multiplica

print(executa(lambda x, y: x+y, 2 , 3))
print(soma(2,3))
print(executa(soma,2,3))


duplica  = executa (lambda m: lambda n: n * m, 2) # nesse caso ela vai executar uma funcao que executa outra funcao
print(duplica(2))         # lambda m: faz refencia a def cria_multiplicador depos a def secundaria lambda n: n*

somar = executa(
    lambda *args: sum(args),
    1, 2, 3, 5, 7, 10
)"""

# para criar uma lambda seria interessante voce fazer uma funcao que executa outra funcao


def execute(funcao, *args): # aqui é uma funcao e um argumento não nomeado
    return funcao(*args)



def soma(*args):
    return sum(args)


print(soma(1, 2, 3, 8, 9))
print(execute(soma, 2, 3, 4)) # aqui é uma funcao que executa outra funcao passando a funcao ser ser executada e seus parametros



create_sum = execute(lambda *args: sum(args), 1, 3, 4)

print(create_sum)


def facto(x):
    return factorial(x)


def executa(f):
   def interna(x):
       valor = f(x)
       return valor
   return interna


factorial1 = executa(facto)
print(factorial1(5))
