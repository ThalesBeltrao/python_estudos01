#super() é a super classe na sub classe
# Classe principal (Pessoa)
# >> super clss, base class, parent class
# Classes filhas (Cliente)
# -- sub class, child class, derived class

class MinhaString(str): # sua classe passa a ser uma string agora contendo todos seus metodos

    def upper(self):
        print("chamou o upper")
        retorno = super(MinhaString, self).upper()
        print("print depois do upper")
        return retorno


#string = MinhaString("luiz")
#print(string.upper())


class A:
    atributo_a = "valor A"

    def __init__(self, nome):
        self.nome = nome

    def metodo(self):
        print("A")


class B(A):  # classe B herda os elemtos de A
    atributo_b = "valor B" # herdamos aqui o atributo_a


    def __init__(self, nome, idade): # se não passar o super no __init__ vai dar erro
        super().__init__(nome)
        self.idade = idade

    
    def metodo(self): # o metodo de B usa ele mesmo por estar com o mesmo nome ele sobreescreve o metodo de A
        print("B")


class C(B):  # classe  C  herda os elemtos de B
    atributo_c = "valor C" #herdamos aqui o tributo_b e o atributo_a

    def metodo(self):
        super().metodo() # agora ele pega o metodo de dentro da funcao da classe B
        super(B, self).metodo() # agora ele pega o metodo de dentro da funcao da classe A
        #super(A, self).metodo() # agora ele pega o metodo de dentro do Object mais la não tem metodo vai dar erro
        # se eu troco por B no super ele vai buscar o metodo de A super = superior classe a cima
        print("C")



c = C("thales",32) # ele herdou tudo o que B herdou de A então agora A tem uma  atributo por isso que pede para passar o atributo na classe C
print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)
print()
c.metodo()
print(c.nome, c.idade)