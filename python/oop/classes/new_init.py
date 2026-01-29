# new e init são metodos para criar classes em objetos
# new responsavel por retornar um novo objeto por isso new recebe cls
# new cria um novo objeto
#__init__ responsavel por inicializar o objeto
#__init__ responsavel por inicializar a instância por isso ele recebe self
#Object é a super classe da nossa classe



class A:
    def __new__(cls, *args, **kwargs): # __new__ ele cria o self ele retorna um objeto(cls)
        print("Antes de criae a inst")
        instancia = super().__new__(cls) # tudo isso é o self do init
        instancia.x = 113

        return instancia



    def __init__(self, x):
        self.x = x
        print("sou o init")

    def __repr__(self):
        return 4 + 2



a = A(1)
print(a.__repr__())
print(a.x)
