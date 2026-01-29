
#x = 10


#def mostrar_valor():
   # global x
    #x = 15
    #print(x)

    #def outra_funcao():
       # x = 11
       # y = 12
       # print(x, y)

    # Quando ela retorna exeecutando não tem a necessidade de voce colocar ela em uma variável
   # return outra_funcao()


# print(x) # aqui vai pegar o valor do 10 por que ele que ele esta executando primeiro
# mostrar_valor()
# print(x) # Pega o valor da variável de fora


# Return ele retorna um valor dentro da funcao
# Para ser guardado dentro de uma variável

#def soma(a, b, *args):
    #return sum((a, b, *args))


# somar_valor = soma(2, 4, 5, 8, 9)
# somar_valor2 = soma(4, 6)

#print(somar_valor + somar_valor2)


# Adiantando - funcao

# Crie uma funcao de Soma


def soma(x, y):
    return x + y


def adiantar_funcao(funcao, x):
    def new_def(y):
        return funcao(x, y)

    return  new_def



resultado = adiantar_funcao(soma, 10)
#print(resultado(15))

# Passand apenas a funcao

#def somatorio(*args):
    #return sum(*args)


#def executa(f):
    #def interna(*args):
        #return f(args)

    #return interna



#result = executa(somatorio)
#print(result(2, 3))


"""Higher Order Funcions"""


# Retornam outras funções, que executam outras ações
# O map é uma delas

def soma(x):
    return x * 2
lista = [1, 2, 3, 4]


resultado2 = list(map(soma, lista))


#print(resultado2)


# Usando lambda para triplicar o valor
resultado3 = list(map(lambda x: x * 3, lista))
#print(resultado3)


# Usando funções que recebem mais de um parametro

def saudacao(msn, nome):
    if not isinstance(msn, str) or  not isinstance(nome, str):
        return "Erro Apenas letras "

    return f"{msn}, {nome}" # dessa maneira ele não retorna uma tupla para você

def executa(f, *args):
    return f(*args)



resultado4 = saudacao("Bom dia","Thales" )
print(resultado4)

resulttado04 = executa(saudacao, "Bom dia", "thales")
print(resulttado04)


# clousure ela passa para a variável executar a funcao

def saudacao2(msn):
    def interna(nome):
        return f"{msn},{nome}"

    return interna


resultado_5  = saudacao2("Boa tarde")
print(resultado_5("Thales"))

