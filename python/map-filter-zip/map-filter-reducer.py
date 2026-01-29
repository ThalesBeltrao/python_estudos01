
from functools import partial,reduce


#map para mapear dados

produtos =[
    {"nome": "p1", "preco": 10},
    {"nome": "p2", "preco": 20},
    {"nome": "p3", "preco": 30},
    {"nome": "p4", "preco": 15},
    {"nome": "p5", "preco": 25.25},
    {"nome": "p6", "preco": 17.5}
]

# Utilizando map com lambda gerando uma lista com os dados modificados sem alterar a lista original
np = list(map(lambda p: round(p["preco"] * 1.1), produtos))
print(np)


# modifica os valores dos dados dos dicionários
nf = [{**p, "preco": round(p["preco"] * 1.1)}for p in produtos]
for p in nf:
    print(p)
print()

# MAP precisa executar uma função pode ser lambda(f=anonimo)
def modificar(item):
    return round(item["preco"] * 1.1)

# apenas trazendo a lista
mf = map(modificar, produtos)
print(list(mf))

# trazendo os dados completo e jogando em uma função, depois passando para o map
def modificar_com_dicionario(item):
    return {**item, "preco": item["preco"] * 1.1}


md = list(map(modificar_com_dicionario, produtos))
p = [p for p in md]
print(*p)