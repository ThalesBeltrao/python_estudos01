import json

class Pessoa:
    ano_atual = 2022  # esse atributo é um padrão para toda instancia que é definida

    def __init__(self, nome , idade ):
        self.nome = nome
        self.idade = idade

    def get_anor_nascimento(self):
        return Pessoa.ano_atual - self.idade


file_json = "../../teste/excercicio.json"


p1 = Pessoa("Adriana", 25)
p2 = Pessoa("Thales", 33)
p3 = Pessoa("Allan", 30)

lista = [vars(p1), vars(p2), vars(p3)]

def dump_json():
    with open(file_json, "w") as file:
        json.dump(lista, file, ensure_ascii=False, indent=2)


dump_json() # como você quer salvar se tu não chama a a função filho de deus 