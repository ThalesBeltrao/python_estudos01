#lista = iter([1, "Thales", 2])
#lista2 = lista
#print(next(lista))
#print(next(lista))
#print(next(lista))


# o iter é um objeto que sabe guardar esses valores que são iteráveis
# na memoria e o next é o objeto que chama por vez cada item que esta dentro do iter()

# como o for fuciona debaixo dos panos

#while True:
    #try:
        #print(next(lista))
    #except StopIteration:
        #break

#print()

#for i in lista2:
    #print(i)


l = [5, 7, 9]
it = iter(l) # Criou um Interador

p1 = next(it) # Aqui você pega o primeiro valor deixando o restante na lista

print("Primeiro elemento da lista", p1) # pega o primeiro elemento da lista
print("Resto da Lista", list(it)) # Converte o restante da lista


# Usando busca e parando conforme a condição alcançada

pegar = (x for x in l if x % 2 == 0)
it1 = next(pegar, None) # quando o elemento não tem retorna None
print(it1)











# Utilizado valores específicos sem a necessidade de percorrer toda a lista
# Utilizando filter ou map


valores = [10, 15, 20, 30]

busca = next(filter(lambda x: x > 15, valores))
#print(busca)
#print(busca)


######################
# Usando filter e map de forma Dinâmica

lista3 = [2, 4, 6]

# Fazendo map para interar sobre todos os valores e fazendo a multiplicação por 2, na lista3
somar = list(map(lambda x: x * 2, lista3))
#print(*somar)

# Filtrar qual valores vai contecer a soma por exemplo se eu quiser apenas mostrar os valores maior que 4

filtrar = list(filter(lambda x: x > 8, somar))
#print(filtrar)


