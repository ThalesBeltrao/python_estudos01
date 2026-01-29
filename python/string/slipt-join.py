# slipt e join com list str
# split -divide uma string
# join - une uma string

frase = "thales, willian, beltrao"
lista_palavras = frase.split(',') # passando para quebrar o texto na virgula
print(lista_palavras[0])

for i in enumerate(lista_palavras):
    print(i)
