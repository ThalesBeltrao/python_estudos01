# Setter atribuir um valor ou modificar um valor de um atributo do objeto


class Caneta:
    def __init__(self, cor):
        self._cor = cor

    @property
    def cor(self):
        print("oi")
        return self._cor

    @cor.setter
    def cor(self, valor):
        print("estou no setter", valor)
        self._cor = valor

    def mostrar(caneta):
        return caneta.cor


caneta = Caneta("Azul")
#getter - Obter valor
caneta.cor = "Rosa"
print(caneta.cor)















from datetime import date

class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def dias_vividos(self):
        return (date.today() - self.idade).days


    @property # get apenas obtenção
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, value):
        if not isinstance(value, date):
            raise ValueError("idade não pode ser uma string, passe apenas usando as virgular ****,**,**")

        self._idade = value




p1 = Pessoa("thales",date(1991, 11, 17))
print(p1.dias_vividos())

p2 = Pessoa("junior",date(1980,12,2))
print(p2.dias_vividos())



#getter retornar uma variavel
#setter definir algo dentro da variavel


# sem funcao decoradora getter e setter
class Projetil:
    def __init__(self, alcance, tempo):
        self.alcance = alcance
        self.tempo = tempo

    def get_velocidade(self):
        return self.alcance / self.tempo


moab = Projetil(1000, 60)
#print(round(moab.get_velocidade()))


# com decorators


class Projetil2:
    def __init__(self, alcance, tempo):
        self.alcance = alcance
        self.tempo = tempo

    @property
    def velocidade(self):
        return self.alcance / self.tempo # como ela ja executasse a ação voce não precisa


#moab2 = Projetil2(1000, 50)
#print(moab2.velocidade)

class Teste:
    def __init__(self, valor):
        self.x = valor



    #def get_valor(self):
        # metodo getter para retornar o valor do atributo x
        #return self.x

    def set_valor(self, v):
        #metodo setter para tribuir um novo valor ao atributo x
        self.x = v


"""
teste = Teste(20)
print(teste.x) # direto do init
#print(teste.get_valor())   #funcao que retorna o valor da instancia da Teste que nesse caso é o valor de x

# usando o setter para atribuir um novo valor ao x
val = int(input("Digite um valor numerico: "))
teste.set_valor(val)
print(teste.x)  #setter coloca um novo adiciona um novo valor na instancia"""


# Setter serve para configuração ou validação em um atributo que é
# Capturado pelo @property

class Produto:
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

