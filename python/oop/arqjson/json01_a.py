

import json
jason = "json01.json"


class Pessoa:
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa("Thales", 32)
p2 = Pessoa("Julia", 23)
p3 = Pessoa("Allan", 28)
bd = [vars(p1),vars(p2),vars(p3)]
def fazer_dump():
    with open(jason, "w") as arquivo:
        print("fazendo dump ")
        json.dump(bd,arquivo, ensure_ascii=False, indent=2)
