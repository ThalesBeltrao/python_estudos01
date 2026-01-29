from math import trunc

from numpy.ma.core import around

# A funcao da list-comprehension serve para modificar uma lista
# e salvar em outra lista fazendo deep copy
# Lembrado que quando você copia uma lista você faz shalow.copy porque ele copia apenas valores imutáveis
# como str, int, float, bool
# para você fazer uma deep.copy você precisa importar copy
# A deep.copy consiste em fazer uma cópia profunda que abrenge
# list, tuple, dict, ‘set’, etc.

# Lista Original
lista = [{ "Produto": "A", "Valor": 29.9},
         { "Produto": "B", "Valor": 10.18},
         { "Produto": "C", "Valor": 15.5},

]

# Lista modificada pelo list-comprehension

#list_update = [{**newlist,"Valor":newlist["Valor"] * 1.05} for newlist in lista]

# Trabalhado com as casas decimal round em list-comprehension

lista_upadte = [{**newlist, "Valor": around(newlist["Valor"] * 1.05, 2)} for newlist in lista]

for i in lista_upadte:
    print(i)