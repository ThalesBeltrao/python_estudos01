from math import sqrt
lista = [
    {"nome": "Thales", "sobrenome": "miranda"},
    {"nome": "Alice", "sobrenome": "Bernadete"},
    {"nome": "Breno", "sobrenome": "Junior"},
    {"nome": "Maiara", "sobrenome": "Roberta"},
    {"nome": "Daniel", "sobrenome": "Queiroz"},

]

list_number = [10, 5, 2, 1, 30]
list_number.sort(reverse=True)  # ela coloca todos os seus elementos em ordem


# print(list_number)

# voce pode passar a funcao no sort para ordenar o dado


def ordenar(item, *args):
    print(item)
    return item[args]  # uma lista que contem dicionários voce acessa dessa maneira pela usuario


# lista.sort(key=ordenar)
# print(lista)

# for i in lista:
# print(i)

def exibir(lista1):
    for i in lista1:
        print(i)
# lambda


lista.sort(key=lambda item: item["nome"])
lista.sort(key=lambda item: item["sobrenome"])

# usando a funcao sorted alem disso ela faz uma copia rasa da sua lista

l1 = sorted(lista, key=lambda item: item["nome"])
l2 = sorted(lista, key=lambda item: item["sobrenome"])



exibir(l1)
exibir(l2)


def executa(funcao, *args):
    return funcao(*args)



def soma(x, y):
    print(x + y)

    return soma


def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplica

    return multiplica



somar = lambda x, y: x+y
# print(somar(2, 3))


# jeitos de retornar um valor

# resultado = executa(lambda x, y: x+y, 2, 3)
# print(resultado)
# soma(2, 3)

# para voce criar uma lambda que recebe um parametro e depois executa
# outra funcao, na pep8 voce tem que criar uma funcao que executa ela


duplica = executa(lambda m: lambda n: n*m, 2)
print(duplica(4))

# print(executa(lambda *args: sum(args), 1, 2, 3))


# fazer uma lambda que retorna a raiz_quadrada

raiz_quadrada = lambda x: sqrt(x)



print (raiz_quadrada(144))

resultado = list(map(lambda x: x * 2.5, list_number))
resultado.sort(reverse=False)
print(resultado)