# Teoria: Métodos Especiais python, Métodos Mágicos ou Métodos Dunder
# Dunder = sublinhado duplo = __dunder__
# Antigo e útil: https://rszalski.github.io/magicmethods/
# https://docs.python.org/3/reference/datamodel.html#specialnames
# __lt__(próprio,outro) - próprio <outro
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(próprio,outro) - próprio - outro
# __mul__(próprio,outro) - próprio *outro
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) -str
# __repr__(self) -str



class Ponto:
    def __init__(self, x, y, z="String"):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"{self.x!r},{self.y!r}, {self.z!r}"  # ele retorna uma representação do seu objeto em string que eta guardado na memoria

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}, {self.x},  {self.y}" # mais voltado para desenvolvedor ele quer ver como seu objeto foi montado


p1 = Ponto(2, 3)
p2 = Ponto(3, 4)


class Ponto2:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.x + other.y
        return Ponto(novo_x, novo_y)



p3 = Ponto2(2, 3)
p4 = Ponto2(4, 5)
p5 = p3 + p4
print(p5)