"""lista em python
 tipo list - mutável
 suporta varios valores de qualquer tipo
 conhecimento reutilizaveis- indice e fatiamento
 metodos uteis:append, insert, pop, del, clear,extend"""


# indice   0   1     2      3   4
lista = [123,True,"thales",1.0,[]]
print((type(lista)))
lista[2] = "joão" # mudando elemento da lista
print(lista)# acessar o indice da sua lista voce coloce [] e acessa o indice

# print(lista[2])
# tipos variaveis Creat(criar), Read(ler), upadate(alterar), delete(excluir) CRUD

#lista = [1,2,3,4,5,10,11]
#numero = lista[2]
#lista[3]=30
#del lista[2]
#print(lista[2])
#print(lista[3])

#lista.append(50)#adicionado ao final da lista
#lista.pop() #remover o ultimo elemento da lista
#print(lista)

#metodos uteis
"""
...append - adiciona elemento oao final da lista   
... insert - Adiciona um item no indice escolhido  
... pop - remove um item do final da lista
... clear - limpar lista
... del - remover um elemento da lista sobre o indice que voce indicar
[-1] sempre o ultimo item da lista
"""
"""lista = [10,20,30,40,50,60,70]
lista.append("luiz") # adiciona elemento ao final da lista
nome = lista.pop()
lista.append("thales")
del lista[-1] # -1 ultimo elemento da lista
#lista.clear()
lista.insert(0,"luiz")# primeiro o indice do elemento e o valor que vai substituir do indice
print(lista)"""

# concatenar as duas lista

# lista1 = [1,2,3]
# lista2 = [4,5,6]
# lista3 = lista1 + lista2
# lista1.extend(lista2)#extender a lista juntar elas
# print(lista1)

# copiando valores
# aponta para o mesmo valor na memória(mutavel)

#  = ["thales","luiz",1,True,1.2]
# lista_b = .copy()#nesse caso voce esta fazendo uma copia a ultimo valor da lista antes dela ser alterada

# [0] = "bruno"
# print()
# print(lista_b)

# lista e for

#lista = ["thales", "willian","Beltrao"]
#indices = range(len(lista))
#for i in indices:
   #print(i,lista[i])

#desempacotamento e empacotamento

#_, _, nome2, *_ = ["thales", "willian","Beltrao","julia"]
#nome1,nome2,nome3 = lista   #cada variavel recebe um valor da lista conforme a sua ordem no indice
#print(nome1)
#print(*_) # o resto ele empacota o restante d alista para não gerar erro caso tenha menos variaveis que quantidade de elementos na lista * serve para desempacotar


# lista dentro de lista
#["Thales", "Maria"], #indice geral 0 indice interno thales[0], maria[1]
    #["Elaine"], #indice geral 1 interno elaine[0]
    #["Luiz","joao","Eduardo"],# indice geral 2 interno luiz[0], joao[1], eduardo[2]
#]

#print(sala[2][2])

#for sala in salas:
    #print(f'A sala numero é {sala}')
    #for alunos in salas:
        #print(alunos)


lista = [1, 2, 3, 4, "thales"]


# Duas maneiras de bucar o índice do elemento
#for i in range(len(lista)):
    #print(i, lista[i])

for i, k in enumerate(lista):
    print(i, k)