#adiando execução de funções

def soma(x, y):
    return x + y


#def multiplica(x, y):
   # return x * y


def executa(funcao, x): #  cria uma funcao e passa o parametro como funcao e um argumento, depois cria outra funcao com um parametro y que retorna o valor da funcao e x então
    # nesse caso o que acontece é quando ele retorna a funcao iterna ele deixa esse valor guardado para ser utilizado quando for executar a variavel que recebe essa funcao
    def interna(y):
        return funcao(x, y)  # faz uma funcao que retorna outra funcao adiando ela

    return interna







soma_com_cinco = executa(soma, 10)
#multiplica_por_dez = executa(multiplica, 10)
print(soma_com_cinco(10))



# adiando execução



def soma(*args):
    return sum(*args)



def executa(f):
    def interna(*args):
        return f(args)
    return interna


somando = executa(soma)
print(somando(2, 3))


# adiando funções com lambda


somando = lambda x: x + 5
resultado = somando(5)
print(resultado)


# funçoes que adiam com map

lista = [1, 2, 3, 4]

doble_list = map(lambda x: x * 2, lista) # x nesse caso é como se fosse um for interator do for passa em cada elemento da lista
retorno = doble_list
print(list(retorno))

print()


def sobrar(x):
    return x * 2.10



lista2 = [2, 3, 4, 5]

multiplicar_lista2 = map(sobrar, lista2)

lista = [1, 2, 3, 4]
double_list = map(lambda x: x * 2, lista)
print(list(double_list))

# com funcao



def dobrar(x):
    return x * 2


trip_list = map(dobrar, lista)
print(list(trip_list))


p1 = [round(p * 2.10) for p in lista2]
print(p1)