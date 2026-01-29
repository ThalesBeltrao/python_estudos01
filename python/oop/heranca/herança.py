# herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição è dono de, herança - È um
#
# Herança vs composição
#
# classe principal (Pessoa)
# super class, base class, parent class
# classe filha(clinete)
# sub class, child class, derived class

# object cria um objeto vazio

class Pessoa:
    cpf = "na classe pessoa"


    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


    def falar(self):
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Cliente(Pessoa):  # herdar a classe pessoa coloca dentro do parentese (Pessoa)
                        # se voce joga a funcao da classe pessoa na classe cliente ele executa em cliente primeiro depois se não tiver pessoa assim por diante
    cpf = " primeiro executo na classe que estou usando" # ele busca sempre na classe que ele esta usando


nome = Cliente("thales", "willian")
print(nome.nome, nome.sobrenome)
nome.falar()  # aqui vai estar mostrando a classe que esta sendo usada
print()
print(nome.cpf)

