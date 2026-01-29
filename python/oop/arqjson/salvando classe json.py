import json
jason = "aula01.json"


class Pessoa:
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa("Thales", 32)
p2 = Pessoa("Julia", 23)
p3 = Pessoa("Allan", 28)
bd = [vars(p1),vars(p2),vars(p3)]

with open(jason, "w") as arquivo:
    json.dump(bd,arquivo, ensure_ascii=False, indent=2)




# classe não é salvo em json