import math as mt
# funcao decoradoras e decoradores
# decorar = adicionar / remover/restringir/ alterar
# decoradores são usados em python
# para as funções decoradoras em outras funções

#def criar_function(func):
    #def interna(*args, **kwargs):
       # print("vou te decorar")
       # for arg in args:
        #    is_string1(arg)
        #resultado = func(*args, **kwargs)
       # print("O seu resultado foi {}".format(resultado))
       # print("ok, agora voce foi decorada")
        #return resultado

   # return interna  # nesse caso voce guarda o valor dela na memoria


#def invert_string(string):
    #return string[::-1]


#def is_string(param):
    #if not isinstance(param, str):
        #raise TypeError("parametro de ser uma string")


#mais_de_um_recurso = criar_function(invert_string)


# invertida = mais_de_um_recurso("123")

# print(invertida)


# decoradores @funcao modo decoradores muito mais simples voce não precisa criar uma variavel e passar a funcao decoradora depois colocar a funcao que vai ser decorada dentro dela dando um trabalho do caralho

#def criar_function(func):
    #def interna(*args, **kwargs):
        #print("vou te decorar")
       # for arg in args:
            #is_string1(arg)
        #resultado = func(*args, **kwargs)
        #print("O seu resultaodo foi {}".format(resultado))
        #print("ok, agora voce foi decorada")
        #return resultado

    #return interna  # nesse caso voce guarda o valor dela na memoria


#@criar_function  # funcao decoradora
#def invert_string(string):
    #print(
       # f"{invert_string.__name__}")  # quando voce coloca um decorador ela pega essa funcao que esta sendo decorada e joga ela na funcao principal usando ela na interna isso faz com que ela mude
    #return string[::-1]



#def is_string1(param):
    #if not isinstance(param, str):
        #raise TypeError("parametro de ser uma string")


# invertida = invert_string("123")

# print(invertida)

# decoradores com parametros
#def fabrica_de_funcoes(fun):
    #print("decoradora 1")

    #def aninhada(*args, **kwargs):
        #print("Aninhada")
        #resul = fun(*args, **kwargs)
        #multiplica = resul * 2
        #return multiplica

    #return aninhada


#@fabrica_de_funcoes
#def soma(*args):
    #return  sum(args)
    #total = 0
    #for i in args:
        #total += i
    #return total


#multiplica = fabrica_de_funcoes(lambda x, y: x * y)


#resultado = soma(10, 5, 6) # aqui sem usar o decorador
#resultado2 = soma(4, 5, 6)
#print(resultado2)# aqui usando o decorador
#print(multiplica(2,6))


# Fábrica de decoradores e fábrica de funções


def fabrica_decoradores(a, b, c):
    def fabrica_funcao(func):
        print("Estou recebendo a funcao")

        def interna(*args, **kwargs):
            print("Ainda não fui decorada")
            resultado = func(*args, **kwargs)
            return interna
    return fabrica_funcao


@fabrica_decoradores(1, 2, 3)
def soma(x, y):
    return x + y




def fabrica_funcao(func):
    print("Estou recebendo a funcao")

    def interna(*args, **kwargs):
        print("Ainda não fui decorada")
        resultado = func(*args, **kwargs)
        return resultado
    return interna

@fabrica_funcao
def soma(x, y):
    return x + y

