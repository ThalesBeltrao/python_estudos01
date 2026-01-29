"""texto = "python"

for letra in texto: #para cada letra no texto exibição
    print(letra"""

#for + Range
# range(start, stop,step)
# for não precisa se preocupar com indice
numeros = range(10)
numeros = range(5,10)# start começo, stop fim, step de quantos em quantos
numeros = range(0,10,2)#
print(numeros)

for numero in numeros:
    print(numero)

"""irerável  str, range,etc (__iter__)tudo aquilo que tem indice
iterador quem sabe entregar um valor por vez for
next me entregue o proximo valor
inter me entregue seu interador"""
print()
texto = "Thales"
iterador = iter(texto)

"""while True:
    try:
        print(next(iterador))
    except StopIteration:
        break"""

for letra in texto:
    print(letra)

# usando for em continue ou break

nome = input("Digite seu nome")

for i in range(4):
   nome = input("Digite seu nome")