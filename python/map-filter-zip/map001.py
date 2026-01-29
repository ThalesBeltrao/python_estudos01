# map serve para mapear dados
# ferramenta para funções

from functools import partial



produtos = [
    {"nome": "produto", "preco": 10.00},
    {"nome": "produto", "preco": 22.32},
    {"nome": "produto", "preco": 7.5},
    {"nome": "produto", "preco": 105.69},
    {"nome": "produto", "preco": 35.99},

]

# Uma maneira usando lambda
#alter_result = list(map(lambda a: a["preco"] * 1.1, produtos))
#tratando_dados = around(alter_result, 2)
#print(tratando_dados)

# Segunda maneira usando list compreenshion
#alter_result = [{**produto, "preco": produto["preco"] * 2} for produto in produtos]
#print(alter_result)


# Terceiro Modo
#def aumentar_porcentagem(valor, porcentagem):
    #return around(valor * porcentagem, 2)

#ele ja define o valor do segundo elemento
#aumentar_dez_porcento = partial(aumentar_porcentagem, porcentagem=1.1)

#new_resultado = [{**p, "preco": aumentar_dez_porcento(p["preco"])} for p in produtos]
#print(new_resultado)

# Usando map


def muda_preco(produto):
    # Faz um list compreenshion aqui
    return [{**produto, "preco": produto["preco"] * 2}]



resultado = map(muda_preco, produtos)
print(resultado)

# Ele está retornando onde o eleemento foi guardado
# Para você saber se um elemento ele é um interator
# voce passa o hasattr e chamando os metodos __iter__, __next__

print(hasattr(resultado, "__iter__"))
print(hasattr(resultado, "__next__"))

# voce pode converter com a lista ou então descompactar os elementos *

#######################

value = [1, 2, 3]
print(list(map(lambda a: a * 2, value)))
