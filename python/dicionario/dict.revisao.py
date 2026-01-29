# dicionario é um tipo de dado que recebe chava e valor

"""pessoa = {
    "Nome": "Thales",
    "Sobrenome": "Willian",
    "Idade": 31,
    "Altura": 1.80,
    "endereços": [
        {"Rua":"Joaquim de Oliveira Silva", "Numero": 1000},
        {"Rua": "Jales Rogruiges", "Numero": 200},
    ]

}

# Acessando valores

print(pessoa["Nome"])

# Acessando valores com get

print(pessoa.get("Peso")) # mesmo que não tenha a usuario ele não quebra
# seu codigo apenas retorna none

print(pessoa.get("Altura"))

# Alterando dicionário ou aterando item

pessoa["Nome"] = "Douglas"
print(pessoa.get("Nome"))

# Adicionando uma nova usuario e um valor

pessoa["Profissão"] = "Analista"
print(pessoa)

# deletando usuario ou valor especificos com pop

pessoa.pop("Profissão")
pessoa["Profissão"] = "Analista"

# Usando del

del pessoa["Profissão"]
print(pessoa)

# limpar deixar o dicionário vazio

#pessoa.clear()
#print(pessoa)

# posso criar uma variavel e transformar ela em uma chava

usuario = "Profissão"

pessoa[usuario] = "Analista"
print(pessoa)

if pessoa.get("Peso", None) is None:
    print("The Key does not exist")

else:
    print("the key exist") """
# values = valor
# key = usuario
# item = usuario e valor
# len = quantas chaves tem
# get = busca se uma usuario é existente no dicionário
# setdefault = adiciona um valor se a usuario não existi
# pop  = apaga uma usuario especifica, pode ser usado para capiturar o valor do item e guardar em uma variavel
# pop.item  = ultimo elemento do dicionário
# upadate = junta dois dicionários
# copy  = retorna uma copia rasa = shallow copy

d1 = {
    "c1": 1,
    "c2": 2,
    "c3": [0, 1, 2]
}

d2 = d1 # ele não faz a copia, ele aponta para o mesmo valor

d2["c1"] = 10 # tudo o que ele fizer vai alterar a lista de d1
print(d1)

# diferente de uma variavel que rebece um valor não mutavel

valor = "thales"
valor1 = valor
valor1 = "joao" # valores imutável ele faz a copia mais quando voce altera ele não reflete na outra variavel
print(valor)

# usando copy

d3 = d1.copy() # ele faz uma copia rasa que só serve para valores imutavel
d3['c1'] = 20
print(d1)

# Nesses casos o que ocorre é que ele copia o dicionario porem se ele alterar a lista dentro dele reflete na original
# por isso chama-se de shallow copy
# para fazer uma deep copy precisa importar um modulo

d3["c3"][0] = 10
print(d1)
print(d3)
# importando o modulo
from copy import deepcopy
# Agora sim temos uma copia profunda ai nesses casos abrange valores imutáveis
d3 = deepcopy(d1)
print()
# Agora sim depois uma deep copi
d3["c3"][0] = 9999
print(d3)
print()


# copi capiturando valores

p1 = {
    "Nome": "Thales",
    "Sobrenome": "Willian",
}

# usado dessa maneira ele copia o valor
#nome = p1.pop("Nome")
#print(nome)
#print(p1)


# update atualização do dicionário

p2 = dict(Endereco="Rua joaquem de oliveira", Numero=1000)
print(p2)

p1.update(p2)
print(p1)

# voce pode sobreescreveer esses valores tambem x:
# criar uma nova usuario
p1.update({
    "Nome": "Allan",
    "Idade": 33
})

print(p1)

p1.update(Altura=1.8)
print((p1))

#  Alterando  o dicionário usando tuplas ou lista

tupla = ("Nome", "novo valor"), ("Sobrenome", "Junior")
p1.update(tupla)
print(p1)
p1.update()

p1["Altura"] = 1.85
print(p1)

