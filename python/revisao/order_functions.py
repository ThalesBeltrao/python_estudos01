# def saudacao(msg):
# return msg


# saudacao_2 = saudacao # voce criou uma variavel para apontar para o valor dela guardado  na memoria
# essa variavel ela pode ser utilizada como uma funcao
# v = saudacao_2("Bom dia") # aqui ele fez uma variavel que aponta para o valor de uma outra variavel que guarda o valor
# da funçao essa variavel ela pode ser usada como uma funcao é como se ocorre o polimorfismo
# print(saudacao_2)
# print(v)
# print(saudacao_2("oi"))


# def saudacao(msg, nome):
# return f"{msg}, {nome}!"


# def executa(funcao, *args): #
# return funcao(*args) # nesse caso ele passa ele executando para a funcao que for passada poder exercer
# suas funções


# v = executa(saudacao, "Bom dia", "thales")
# print(v)

# outro modelo de order function


# def aplicar_operação(operacao, numero):
# return operacao(numero)


# def quadrado(x):
# return x ** 2


# resultado = aplicar_operação(quadrado, 5)
# print(resultado)

# funcao dentro de funcao


# def multplicao(fator):
# def valor(numero):
# return numero * fator

# return valor


# resultado = multplicao(...)
# print(resultado(...))

# soma = lambda x, y: x + y
# print(soma(2, 3))

# exemplo


# def  quadrado(valor):
# return valor ** 2


# resultado = quadrado(5)
# print(resultado)

# lambda

# quadrado2 = lambda x: x ** 2
# print(quadrado2(5))


# lista10 = [2, 3, 4, 8, 10]
# resultado10 = map(lambda x: x * 2, lista10)
# print(list(resultado10))


# Clousure e funções que retornam outras funçoes
# como padrão a funcao ela executa o valor da funcao interna e não salva ela na memoria
# ja o clousure ela faz com que a variavel que voce passou a funcao seja a propria funcao para voce
# chamar quando quiser


#def externa():
    #msg = "Ola, bom dia"

    #def interna1():
        #print(msg)

    #return interna1


#s1 = externa()

# clousure é fazer uma variavel executar diretamente a funcao interna voce guarda ela


def multiplica(valor):
    #valor = float(input("Digite um numero: "))

    def valor_passado(novo_valor):
       print(valor * novo_valor)

    return valor_passado



# duplica = multiplica(2)
# triplica = multiplica(3)
quadriplica = multiplica(4)

# print(duplica(2))
# print(triplica(3))
# print(quadriplica(4))

#for i in [2, 3, 4]:

    #quadriplica(i)

lista = [10, 20, 30, 40, 60]

resultado = list(map(lambda x: x * 2, lista))

dez, vinte, *_ = resultado

for i in list(enumerate(resultado)):
    nova_lista = list(i)
    print(nova_lista)


resultado2 = [dez, 10,]
resultado2.extend(_)
print(resultado2)