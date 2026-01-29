# def adicionar_a_lista(lista, *valor):
    # colocar_valor = int(input("Digite um valor: "))
    # valor = colocar_valor
    # ista.append(valor)

    #print(lista)

# Exemplo de uso


# minha_lista = []
# while True:
    # adicionar_a_lista(minha_lista)



# argumentos nomeados e não nomeados



# def soma(x, y, z): # paramtr
    # print(x + y + z)


# soma(2, 3, 4) # vai dar erro porque a funcao ela pede uma posição que tem que ser passada para o parametro
# soma(y=2, x=3, z=2) # argumento

# def de definição da funcao
# soma # nome, mas sem execução
# soma() funcao sendo executada

# valores padrão para parametro
# Ao definir uma funcao, os para
# quando voce vai refatorar = editar seu codigo



# def soma(x, y, z=None):
    # if z is not None:
        # print(f'{x=} {y=} {z=}', x+y+z)
    # else:
        # print(f'{x=} + {y=} ==', x+y)


# soma(1, 2, 10) # porque esta dando errado ? não esta retornando a primeira funcao ?
# porque O no if quando destado ele é falso  é um não valor igual vazio ou None
# então ele sempre vai retornar o else do teste


"""
Escopo de funcao em python
escopo significa o local onde aquele código pode atingir 
Existi o escopo global e local 
O escopo global é o escopo onde apenas nomes do mesmo local 
podem ser alcançados.
"""



# def escopo():

    # print(x)

# print(x) não tem como você acessar a variavel de dentro da funcao fora dela
# o escopo da funcao só pode acessar valores externos e nao internos

# escopo()
x = 1


# def funcao():
    # global x
    # x = 10   # eu consigo acessar o que esta fora
                # eu não consigo buscar sobre a funcao interna nenhum valor como regra

    # def nova_funcao():
        # global x
        # z = 20
        #x = 15
        #print(x, z)

    # nova_funcao()
    # print(x)


#funcao()

# def interna():
    # print("iniciando a funcao interna")
    # return 42


# def externa():
    # print("Iniciando funcao externa")
    # resultado = interna()
    # print("Resultado da funcao interna {}".format(resultado))
    # print("Finalizando a funcao externa")


# externa()

# Return retorno da funcao

# como regra as funções elas retornam none
# o que é um none, um none é um não valor, como vazio
# 0 é um none, não zero em boleano é False e se colocar em uma variavel ele é um numero inteiro
# um não valor são [], (), {}, "",
# o none voce pode especificar um valor para ele para que ele deixe se ser none e passa ater um valor de referência

def soma_2(z, y):
    return z + y #apenas funcao e metodos tem return
    # return ele alem de jogar esse valor em uma variavel ele mata a funfão
    # nada a baixo dele é executado




soma12 = soma_2(2, 3)
soma2 = soma_2(4, 3)
# para eu poder salvar essa funcao em uma variavel eu preciso retornar esse valor

# print(soma2 + soma12)
# esta dando erro porque essa funcao não retorna nada, quando voce salva ela em uma variaval

# soma_2(2, 3)


# def multiplication(a, b):
    # return a * b


# def area(valor=input, base=input, altura=input):
    # valor = input("Qual area você quer calcular quadrado, retangulo, triangulo: ").strip()
    # if valor == "quadrado" or valor == "Quadrado":
        # base = float(input("Digite o valor da base: "))
        # area_calculada = multiplication(base, base)
        # print(f"O valor da area do quadrado {area_calculada} ")
        # print("a area do quadrado é feita pela base * base")

    # elif valor == "retangulo" or valor == "Retangulo":
        # base = float(input("Digite o valor da base: "))
        # altura = float(input("Digite o valor da altura: "))
        # area_calculada = multiplication(base, altura)
        # print(f"O valor da area do retangulo é {area_calculada}")
        # print("A area do retangulo é feita pela multiplicação da Base * Altura")

    #elif valor == "triangulo" or valor == "Triangulo":
        #base = float(input("Digite o valor da base: "))
        #altura = float(input("Digite o valor da altura: "))
        #area_calculada = multiplication(base, altura) / 2
        #print("O valor do triangulo é {}".format(area_calculada))
        #print("O valor da area do triangulo é feita pela Base * Altura dividida por 2")






#while True:
    #valor = input("deseja sair ou entrar: ").strip()

    #if valor == "entrar" or valor == "Entrar":
        #area()
    #elif valor == "sair":
        #break


# args argumentos não nomeados

# *args(empacotamento e desempacotamento)

t, y, * resto = 1, 2, 3, 4, 5
#print(t, y, resto) # aqui ele esta empacotado como lista
# porem voce pode desempacotar chamando em uma funcao
#print()
#print(t, y, *resto)


#def soma(*args):
    #total = 0
    #for numero in args:
        #total += numero

    #return total


#valor_soma = soma(2, 3, 4)
#print(valor_soma)


# pode se usar a funçao sun para *args

#def soma(* args):
    #return sum(args)


# valor_soma = soma(2, 4, 8)
# vrint(valor_soma)

#def soma(*args):
    #valor = 0
    #for numeros in args:
        #valor += numeros
    #return valor


# tupla = 1, 2, 3, 4
# novo_valor = soma(*tupla) # se eu não desempacotar vai dar erro, porque vai vai fazer outra tupla dentro de outra tupla
# print(novo_valor)

