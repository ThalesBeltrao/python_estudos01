#Exercícios:
#Transforme a string "maçã,banana,laranja" em uma lista de frutas.
#A string "10;20;30;40" deve ser transformada em uma lista de números (como inteiros).
#Separe cada palavra da frase "Eu gosto de estudar Python" e conte quantas palavras têm na frase.

# Exercicio 1
frutas = "mala, banana, laranja".split(",")
tira_espaco = [i.strip() for i in frutas]
print(frutas)
print(tira_espaco)


# Exercio 2
n1 = "10;20;30;40".split(";")
convercao = list(map(int, n1)) # utilizando map
print(convercao)
print()

convercao2 = [int(i) for i in n1] # utilizando listcomprention
print(convercao2)

#Exercio 3

frase = "Eu gosto de estudar Python".split()
print(len(frase))
