"""list comprehension
mapeamento de dados

lista = []
for numero in range(10):
    lista.append(numero)

lista = [
    numero * 2
    for numero in range(10)
]
print(lista)



produtos =[{"nome": "p1", "preco":10},
           {"nome": "p2", "preco":20},
           {"nome": "p1", "preco":30}

]"""
#print()
#maperamento de dados
# detalhes do mapeamento  o mapeamento serve apenas para números e vem à esquerda do for
# alteracao_valor = [{**produto, "preco": produto["preco"] * 1,05}
                   #if produto["preco"] > 20 else{**produto} # nesse caso ele faz um if antes isso é mapeamento serve apenas para numeros
                   #for produto in produtos
#]

#print(*alteracao_valor, sep="\n")

# filtro vem à direita do for e não precisa do else

# fazendo filtragem na list comprehension

lista = [n for n in range(10) if n <5]
print(lista)

produtos =[{"nome": "p1", "preco":10},
           {"nome": "p2", "preco":20},
           {"nome": "p3", "preco":30},

]

novos_produtos = [
    {**produto,"preco": produto["preco"] * 1.05} # aplicando um map dentro do list-comprehension
     if produto["preco"] > 10 else{**produto}
    for produto in produtos
    if produto["preco"] > 10 # aplicando um filter dentro da lis-comprehension

]

print(novos_produtos)
print()
preco_alterado =  [{**produto, "valor_alterado": produto["preco"] * 2} for produto in produtos]
print(*preco_alterado, sep="\n") # se voce não passa o mesmo nome da usuario, ela não sobre escreve o valor e cria uma outra variaável
# com o valor alterado