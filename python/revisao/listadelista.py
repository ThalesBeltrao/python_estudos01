salas = [
    ["Maria", "helena"], # indice 0 dentro da lista dentro do indice [0][0], [0][1]
    ["Thales", "Junior", "Alex"],
    ["Luiz", "João", "Mario", "Rodolfo", (10, 20, 30)]
]

#print(salas[2][4][2])

#for i in salas:
    #print(i)
    #for item in i:
        #print(item)

print(*salas, sep="\n")  # ele quebra as listas uma de baixo da outra

print("Python é Legal", end=" ")
print("Python é bom ") # ele deixa os prints na mesma linha e não em blocos


# ordenar uma lista

list_number = [99, 30, 20, 5, 3]
#print(sorted(list_number))

# uma outra forma e chamar a funcao da classe mesmo

list_number.sort(reverse=False)
print(list_number)