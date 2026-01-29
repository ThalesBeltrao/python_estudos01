import json

from json01_a import jason, Pessoa,fazer_dump

with open(jason, "r") as arquivo:
    dados = json.load(arquivo)
    #print(dados)

#fazer_dump() # nesse vcaso voce pode fazer ações dentro desse modulo porque agora a classe virou um funcao então voce pode adiar ações
p1 = Pessoa(**dados[0])
p2 = Pessoa(**dados[1])
p3 = Pessoa(**dados[2])

print(p1.nome, p1.idade)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)