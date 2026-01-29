#Atributos de Classes
class Pessoa:
    ano_atual = 2025  # esse atributo é um padrão para toda instancia que é definida

    def __init__(self, nome, idade ):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


nome1 = Pessoa("thales", 33)
print(nome1.nome, nome1.idade)
print(nome1.get_ano_nascimento())