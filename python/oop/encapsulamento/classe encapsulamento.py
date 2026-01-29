#convenções
#(sem underline) = public
#_ (um underline) = protected não deve ser usado fora da classe
# __ (dois underline) private so usada na classe em que foi declarada



class Foo:
    def __init__(self):
        self.public = "isso é publico"
        self.protected = "isso é protegido "

    def metodo_publico(self):
        return "oi"


f = Foo()

#print(f.protected) # por estar protegido eu não posso usar fora da classe  ou sub classe
#print(f.public)
#print(f.metodo_publico())

