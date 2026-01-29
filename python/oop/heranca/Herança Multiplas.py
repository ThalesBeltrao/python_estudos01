# Herança Multipla - Python Orientado a Objeto
# Quer dizer que no Python, uma classe pode estender
# varias outras classes
# Herança simples:
# Animal > Mamifero > HUmano > Pessoa > Cliente
# Herança Multiplica e mixins
# log > filelog
# Cliente(Pessoa, Filelog)

# Python 3 usa c3 superclass linearization
#para gerer o mro
#voce não precisa estudar isso (é complexo)


# para saber a ordem de chamada dos metodos
# use o metodo de classe Classe.mro()
# Ou o atributo: _mro_ (dunder - Double - Underscore)


class A:
    ...

    def quem_sou(self):
        print("A")


class B(A):
    ...

    #def quem_sou(self):
        #print("B")


class C(A):
    ...

    def quem_sou(self):
        print("C")


class D(B, C):
    ...

    #def quem_sou(self):
        #print("D")


d = D()
d.quem_sou()

print(*D.__mro__)
print()
print(*D.mro()) # para voce achar as heranças que ele tem e caso uma seja apagada qual herança ele ira herdar

# quando mais voce tiver mais herança multiplas voce vai se foder para depois achar o caminho


