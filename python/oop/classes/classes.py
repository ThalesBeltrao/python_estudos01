# class - Classes sao moldes para criar novos objetos
# as classes geram novos objetos(instancias)
# podem ter seus proprios atributos(dados) e metodos(ações)
# Os objetos geradsos pela classe podem usar seus dados
# internos para realizar varias ações
# por conveção, usamsos PascalCase para nomes de
# classes


class Pessoa:
    ...

p1 = Pessoa()
p1.nome = "luiz"
p1.sobrenome = "Otavio"
print(p1.nome,end=" ")
print(p1.sobrenome)
print()

# __init__ inicializador de objeto
class Pessoa:
    def __init__(self, nome, sobrenome): # self ele é a variael p1 fora da classe
        self.nome = nome
        self.sobrenome = sobrenome

#p1 = Pessoa("thales", "wilian")

print(p1.nome, p1.sobrenome)

#repara que nesse caso só tem parametros não temos metodos a sua classe não executa nenhuma ação ()

# Metodos

class Carro:
    def __init__(self, modelo):
        self.modelo = modelo

    def ligar(self, modo): # ligando passar um argumento para a instância na hora que for executar
        return f"{self.modelo} esta no modo: {modo} "

    def modo(self, *args):
        return self.ligar(*args) # aqui define o modo que vai ser passado para instância


#carro = Carro("Ford")
#print(carro.modo("Hibrido"))

# Colocando um Valor padrão
# Caso nenhum argumento seja passado para a instância

class Carro1:
    def __init__(self,modelo):
        self.modelo = modelo
        self._modo = None

    def __int__(self,modelo,  modo):
        self.modelo = modelo
        self._modo = None # porque voce define um valor padrão

    def ligar1(self, modo="Gasolina"):
        self._modo = modo
        return f"{self.modelo} esta no modo {self._modo}"

    def modo(self, *args): # pode passar qualquer modo aqui
        return self.ligar1(*args) # deixa aberto passar outros parametros


carro = Carro1("ford")
print(carro.ligar1("Hibrido"))