frase = " Olha só que, coisa interessante"
lista_palavras = frase.split(",") # pega a frase e dividi pelos espaços e coloca ela dentro de uma lista.
print(lista_palavras)
# no caso do split pode haver casos em que voce pode passar onde ela tem que dividir

lista_palavras2 = frase.split(",")
print(lista_palavras2)

lista = []
for i, frase in enumerate(lista_palavras):
    lista.append(lista_palavras2[i].strip())

#print(lista_palavras2)
#print(lista)

frases_unidas = "-".join("abc") # crie uma string vazia e chama o join
print(frases_unidas)

