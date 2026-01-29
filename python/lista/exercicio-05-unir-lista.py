# exercicios - unir lista
# crie uma funcao zipper
# o trabalho dessa funçao sera unir essas lista

def zipper(lista1, lista2):
    intervalo_maximo = min(len(lista1), len(lista1))
    return [
        (lista1[i], lista2[i])for i in range(intervalo_maximo)
    ]


l1 = ["Salvador", "ubatuba", "Belo Horizonte"]
l2 = ["BA", "SP", "MG", "RJ"]

print(*zipper(l1, l2),sep="\n")
print()

# outra maneira unir lista
l1 = ["Salvador", "ubatuba", "Belo Horizonte"]
l2 = ["BA", "SP", "MG", "RJ"]

print(*list(zip(l1, l2)), sep="\n")
print()
"""somar duas listas de inteiros 
se uma for menor so vai considerar a da menor """

lista_a = [1, 2, 3, 4, 5]
lista_b = [1, 2, 3, 4]
#lista_soma = []
#primeiro modulo
#for i in range(len(lista_b)): dessa maneira voce mostra o indice igual enumerate
    #lista_soma.append([i] + lista_b[i])
#segundo modulo
#for i, _ in enumerate(lista_b):
    #lista_soma.append([i] + lista_b[i])
#print(lista_soma)
#print()
# terceito modulo
lista_soma = [x + y for x, y in zip(lista_a, lista_b)]

print(lista_soma)

