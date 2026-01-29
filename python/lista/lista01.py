lista = ["Thales", 2, 5.3, bool]
#lista.insert(2, "Thais")  # insert ele especifica qual indice voce quer colocar o elemento
lista01 = [ "Ivan", 33]

lista2 =  lista01 + lista

#print(lista)
#print(lista2)

# append ele insere um elemento ao final da lista , seja um unico elemento ou uma cadeia de elementos

#lista.append([10, 11, "Junior", (1, 2, 3)])
#print(lista[5][3][1])

# ja o extend ele desempacota os interaveis
#lista.extend(["João", 1.1]) # por exemplo voce pega uma lista e quer desempacotar para colocar dentro de outra lista
# nesses casos o ideal a se fazer é justamente extend
#print(lista.pop()) # remove item ao final da lista
#print(lista)
#del lista[2] # deleta passando o indice da lista
#print(lista)

#print(lista2[0][0:4]) # voce pega o indice e dentro dele o indice do caracteres que voce quer buscar nesse exemplo

# alterar elemento da lista

lista[2] = "Janaina"
# lista.clear()
# print(lista) # limpa todos os elementos de dentro da sua lista

# print(lista2)

# pop retira do elemento da lista voce pode salvar ele em uma variavel
# Exemplo

salve_pop = lista2.pop(3)
# print(f"{salve_pop}, = {type(salve_pop)} ")
# print(lista2[-1]) # -1 sempre sera o ultimo elemento da lista
# print(lista2)
list_new = ["Junior", 10.2, 5, bool]
#lista_3 = lista01.extend(list_new) # ele faz o desempacotamento de uma lista dentro de outra lista
#print(lista_3) # extend ele não retorna um valor ele apenas modifica o valor da variavel então ele vai retornar um NONE


#corrigindo erro primeiro modo
lista_3 = lista2.copy()
lista_3.extend(list_new)
print(lista_3)

# corrigindo erro segundo modo

# lista_3 = [*lista2, *list_new] # desempacotamento, mesma funcao do extend que desempacota uma lista dentro de outra lista
# print(lista_3)

# corrigindo erro terceira maneira
# print(lista_3)



# copy
""" cuidado com dados mutaveis 
copiando o valor (imutável) aponta para o mesmo valor na memoria(mutável)"""
nome = "Thales"
outra_variavel = nome # aqui ele salva esse valor na memoria "Thales"
nome = "João" # a variavel nome ela foi sobreescrita
print(nome)
print(outra_variavel)

# agora com lista é diferente

lista_a = ["Luiz", "Maria"]
# lista_b = lista_a
# valores mutavel nesse caso voce aponta para o mesmo valor na memoria
# qualquer alteração que voce fizer na lista a vai refletir na lista b
# print(lista_b)
# lista_b = lista_a.copy()
# lista_a[0] = "Junior"
# print(lista_b)
# print(lista_a)
# para voce não fazer com que a sua lista b aponte para o mesmo valor da lista a
# voce precisa fazer uma copia
print()
# for em lista
#contador = 0
#for i in lista_a:
    #print(contador, i)
    #contador += 1

# outro modo de resolver

indice = range(len(lista_a)) # vai contar o tamanho da lista
print(indice)
print(lista_a)

#for i in indice:
    #print(i, lista_a[i])

# ele busca o indice da sua lista e vai interar sobre cada elemento da sua lista usando esse indice

# Exemplo
#indice_2 = [0, 2, 3]
#lista_letra = ["a", "b", "c", "d", "e"]

#for i in indice_2:
    #print(i, lista_letra[i]) # aqui voce pega um valor da sua lista e passa o indice do for para buscar esses valores
    # i no caso ele vai percorrer cada valor do indice_2 depois voce vai chamar o a lista e vai usar [i]para interagir sobre a sua lista

#print(range(len(lista_letra)))

nome1, nome2, *_ = ["Thales", "Willian", "Beltrao", "thais", "Fernanda"] # nesse caso em empacotei o beltrao na variavel a
print(nome1, nome2,_[0], _[1], _[2])


# tuple é uma lista imutável

tupla = (1, 2, 3, 4)
tupla01 = "Thales", "Willian", "Beltrao"

print(type(tupla01))

# enumerate interação mostra o indice de uma lista enumerada
# ele é um tipo de interador  podendo chamar next nele

#lista_enumerada = enumerate(lista_a)
#print(list(lista_enumerada)) # ele apenas apresentou o valor que esta guardado na memoria ele precisa
# do for ou chamar o next nele para ele interagir com o indice da lista
print()

for i, valor in enumerate(lista):
    print(i, valor)

print(*lista[5])