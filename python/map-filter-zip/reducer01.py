# Reduce faz a redução de iterável em um valor
# Ela tem que ser importável

from functools import reduce

produtos = [
    {"nome": "produto", "preco": 10.00},
    {"nome": "produto", "preco": 22.32},
    {"nome": "produto", "preco": 7.5},
    {"nome": "produto", "preco": 105.69},
    {"nome": "produto", "preco": 35.99}

]
def reducao(acumulador, produto):
    print("acumulador", acumulador)
    print("produto", produto)
    return acumulador + produto["preco"]


reduzir = reduce(reducao, produtos, 0)


# Acumulador
#valor = 0

#for i in produtos:
    #valor += i["preco"]


# Usando um somário e listcompreenshion
#resultado2 = sum(n["preco"] for n in produtos)
#print(resultado2)


