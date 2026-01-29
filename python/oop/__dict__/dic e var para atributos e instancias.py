import json
import json as js
class Pessoa:
    ano_atual = 2022  # esse atributo é um padrão para toda instancia que é definida

    def __init__(self, nome , idade ):
        self.nome = nome
        self.idade = idade

    def get_anor_nascimento(self):
        return Pessoa.ano_atual - self.idade


nome1 = Pessoa("thales", 32)
print(nome1.__dict__) # onde esta guardado a usuario e o valor da sua classe
nome1.__dict__["altura"] = 1.80 # __dic__ e é editavel
print(nome1.__dict__)
print(vars(nome1)) # tambem mostra o dicionário
print(nome1)
# salvando os dados de uma classe em um dicionário



class Pessoa:
    ano_atual = 2022  # esse atributo é um padrão para toda instancia que é definida

    def __init__(self, nome , idade ):
        self.nome = nome
        self.idade = idade

    def get_anor_nascimento(self):
        return Pessoa.ano_atual - self.idade

dados = {'nome': 'thales', 'idade': 32}
p1 = Pessoa(**dados) # esta desempacotando os dados que é o mesmo que passados na classe
#p1 = Pessoa("thales", 32)
#print(vars(p1))
#print(vars(p1))
print(p1.nome) # nesse caso ele busa do dado da lista ja desempacotado

salve_json = js.dumps(p1.__dict__)
print(salve_json)

with open("../arqjson/arquivo1.json", "w") as escrita:
    js.dump(p1.__dict__, escrita)