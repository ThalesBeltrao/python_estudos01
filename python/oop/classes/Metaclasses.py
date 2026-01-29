# Metaclasses são o tipo das classes
# Em Python, tudo é um objeto
# Classes também são objetos
# seu objeto é uma instancia da sua classe
# sua classe é uma instancia de type(type é uma metaclasse)

# Ao criar uma classe, coisas ocorrem por padão nessa ordem
# __new__ da metaclass é chamado e cria a nova classe
# __call__ da metaclasse é chamado com os argumento e (cria instancia)
# __new__ da class com os argumentos ( cria instancias)
# __init_ da class com os argumentos
# __call__ da metaclasse termina a execução
####
# Métodos importantes da metaclass

# __new__(mcs, name, bases, dct) ( cria classes)
# __call__(cls, *args, **kwargs) ( cria e inicaliza as intancias)


# object esta acima da classe e type esta acima de objetct
# print(type(f))
class Meta(type):
    ...



class Pessoa(metaclass=type):
    def __new__(cls, *args, **kwargs):
        print("Meu New")
        instancia = super().__new__(cls)
        return instancia

    def __init__(self, nome):
        print("Meu Init")
        self.nome = nome


p1 = Pessoa("Luiz")