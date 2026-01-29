# Funções recursivas e recursividade
# - Funções que podem se chamar de volta
# úteis para dividir problemas grandes em partes menores
# Toda função recursiva deteve ter:
# Problemas que possa ser divididos em partes menores e uniformes
# Um caso recursivo que resolve o pequeno problema
# U|m caso base que para a recursão
# fatorial n! = 5 * 4 * 3 * 2 * 1 = 120

#def recursiva(inicio=0, fim=10):
    # Caso Base
    #if inicio >= fim:
        #return fim
    # Caso recursivo
    # Contar até chegar ao final

    #inicio += 1
    #return recursiva(inicio, fim)


#print(recursiva())


#def lista_recursiva(lista):
    #if not lista:
        #return 0

    #return lista[0] + lista_recursiva(lista[1:])



#numero = [1, 2, 3]

#print(lista_recursiva(numero))

# fatoração usando recursividade

def fatorial(valor):

    if valor == 0:
        return 1

    return valor * fatorial(valor - 1)


fator = fatorial(5)
print(fator)