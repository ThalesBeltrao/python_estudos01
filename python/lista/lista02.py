lista1 = [1, 2, 3, 4]
lista2 = [2, 2, 4, 4]
lista1.append(3) # o elemento vai para o final da fila
lista2.append(7)
lista1.append(8)
lista3 = lista1 + lista2
# print(lista3)

a = [1]
b = a
# append adiciona o elemento no ultimo local da lista
b.append(2)
# print(a) # quando voce faz uma variável que aponta para o mesmo local tudo que voce muda nela ou na original interfere nas duas

# alterar um elemento em uma posição específica
# a[0] = 2
# print(a, b,)

# insert ele coloca outro elemento na posição que você indicar porem ela não sobreescreve o elemento
# ela apenas coloca ele na posição, e o que foi trocado vai para o final

a.insert(1, "thales") # index(posição) e depois o objeto
# print(a)

# del

del a[2]
# print(a)
a.insert(2, 2)
# print(a)

del a[-1] # o ultimo elemento ou o primeiro da direita para a esquerda
#print(a)

# Concatenando duas lista

a1 = [1, 2, 3]
a2 = [4, 5, 6]
a3 = a1 + a2
# print(a3)

# usando extend
a1.extend(a2)
# print(a1)


# copiando valores apontando para o mesmo valor na memória
# porem esse vaor ele não altera o vaor original

lista_a = ["thales", "luiz", 1, True, 1.2]
lista_b = lista_a.copy() # a lista original foi copiada

lista_a[0] = "bruno"
# print(lista_b) # percebe-se que a lista original ela não se modifica, porque eu fiz uma copia e nao um apontamento

# for em lista
# indices

indices = range(len(lista_a))
print(indices) # 5 elementos indices 0 a 4
# o indice ele sempre é a quantidade de elemento menos -1
# porque ele começa no 0

# for i in indices:
    # print(i,lista_a) # aqui ele nao intera no elemento em si mas sim na lista cria 5 indices para cada lista
lista_a = ["thales", "luiz", 1, True, 1.2]
indices = range(len(lista_a))
for i in indices:
    ...#print(i,lista_a[i])

#print()

# desempacotar e empacotar 


_, _, nome2, *_ = ["Thales", "Julia", "Allan", "Tersinnha"] # *_ serve para empacotar o restante da listan
lista10 = ["Thales", "Julia", "Allan", "Tersinnha"]
nome0, nome1, *_ = lista10 # ele guarda na memoria os os indices correspondentes com as variaveis no caso nome0 faz referência ao thales
# e assim por diante
# *_ ele guarda o restante do indice na memoria e quando você chama ele com o print
# você pode passar o indice dele que no caso seria *_[0] = Allan e *_[1] Teresinha

# somando  duas listas

l1 = ["Salvador", "ubatuba", "Belo Horizonte"]
l2 = ["BA", "SP", "MG", "RJ"]

somarlist = list(zip(l1, l2))

# somando duas listas inteiras

numeros0 = [1, 2, 3, 4, 5]
numeros1 = [6, 7, 8, 9, 5]

# Apenas numero de colunas iqual com valores se uma lista for maior que a outra
# O zip equaliza os valores excluindo os elementos que sobram
soma_lista = [x + y for x, y in zip(numeros0, numeros1)]
print(soma_lista)

# map serve para alterar um valor de uma lista
modify = list(map(lambda x: x * 1.5, numeros0))
print(modify)

# Exemplo eu quero buscar apenas valores superiores de 3
filtro = list(filter(lambda x: x > 3.0, modify))
print(filtro)



