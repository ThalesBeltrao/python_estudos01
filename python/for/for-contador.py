#Fazer um somador usando for

"""somatorio = 0
lista = []
for i in range(1, 5):
    somatorio += i
    lista.append(i)

#print(somatorio)

#print(sum(lista))

# Usando for range e len
# Para criar indices e acessar os elementos por eles

lista1 = [10, 20, 30, 40]

for i in range(len(lista1)):
    #print(f"{i}: {lista1[i]}")
    ...
print()

# Modificação da lista
for l in range(len(lista1)):
    #print(lista1[l] * 2)
    ...
# Uma forma mais pytonica usando enumerate
for l1, v1 in  enumerate(lista1):
    #print(l1, v1)
    ...
"""
# Percorrendo uma Matriz

matriz = [["Nome", "Idade", "Altura"],
          ["Thales","33","1.8",],
          ["Junior","38","1.8"]

          ]

# Percorrendo Linha e Elemento

for l in matriz: # Busca a linha
    for v in l:
        print(v, end=" ") # busca os elementos da linhas
    print() # Quebra de linha para formar a matriz

print()
#Acessando com índice
# Serve para modificar valores

#for i in range(len(matriz)):
    #for c in range(len(matriz[i])):
        #print(matriz[i][c], end= " ")
    #print()

# Modificando Valores

for i in range(len(matriz)):
    for c in  range(len(matriz[i])):
        if i == 1 and c == 2:
            matriz[i][c] = "2.0"

print(*matriz, sep="\n")


# Usando enumerate

