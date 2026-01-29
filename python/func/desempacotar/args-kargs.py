import math
"""
args - argumentos não nomeados
*- *args(empacotamento e desempacotamento)

"""

#x, y, *resto = 1, 2, 3, 4
#print(x, y, resto)# x, y desempacotamento e *resto empacotamento
#print()

#def soma(*args):# args argumentos não nomeados voce não passa nenhum parametro para a funcao não passa uma quantidade especifica
    #somatorio = sum(args)# args dentro da funcao é uma variavel empacotadora
    #print(somatorio)
   # args = list(args) # nessa caso os valores passados para a funcao soma é uma tupla por isso saõ invariaveis então faz-se a conversão para lista
   # print(args, type(args))
#soma(1,2,3,4,5,6) # nesse caso não gera erro porque a funçaõ foi definida como parametro args ela esta empacotando
            #  ela esta definindo toda a funcao
#def soma2(*args):
    #args = list(args)
    #total = 0
    #for i in args:
       # total += i
   # print(total) # nesse caso a funcão print ela mostra o valor exibido do resultado da funcão quando chama ela
    #return total # nesse caso não vai aparecer nada se voce não jogar esse valor do total lem uma variavel e depois printar ela porque o return ele guarda esse valor para ser colocado em uma variavel fora da funcao

#sominha = soma2(1 ,2, 3, 4, 5, 6) # nesse caso ele esta com o return esse valor esta salvo na memoria e toda vez que isso acontece por causa do return tem que salvar ele na memoria
#print(sominha)


#numeros = 1, 2, 3, 70, 50
#outra_soma = soma2(*numeros)
#print(soma2(*numeros))
#print(sum(numeros))
#print(outra_soma)

# 1-) Crie uma funcao que multiplique os argumentos não nomeados
# 2-) Crie uma funcao que fala se o numero é impar ou par



def multiplica(*args):
    total = 1 # quando for multiplicaçao tem que fazer pelo 1 e soma por 0
    for i in args:
        total *= i
    return total # nesse caso por ter o return voce tem que salvar o  resultado da funcao em uma variavel e depois chamar print para mostra o resultado da funcao

valores_multiplicados = multiplica(2,4,2,8,4)
print(valores_multiplicados)
print()
def mulplica2(*args):
    total = 1
    for i in args:
        total *= i
    print(total) # nesse caso esse valor não é salvo em uma varial igual o return então voce chama a funcao e depois passa os argumentos para ela executar a funçao


mulplica2(2, 2)


def par_impar(*args):
    valor = int(input("Digite um valor: "))
    valor2 = valor % 2 == 0

    if valor2 == 0:
        print("Esse valor é par ")
    else:
        print("Esse valor é impar")

par_impar()
