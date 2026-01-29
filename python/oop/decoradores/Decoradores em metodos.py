def add_repr(cls):
    def my_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f"{class_name} ({class_dict})"
        return class_repr

    cls.__repr__ = my_repr
    return cls


def my_planet(metodo):
    def interno(self, *args, **kwargs):
        resultado = metodo(self, *args, **kwargs)  # resultado da instancia

        if "Terra" in resultado:
            return f"você esta em casa {self.nome}"
        return resultado

    return interno


@add_repr
class Time:
    def __init__(self, nome):
        self.nome = nome


@add_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome

    @my_planet
    def falar_nome(self):
        return f" O planeta é {self.nome}"


brasil = Time("Brasil")
portugal = Time("Portugal")
terra = Planeta("Terra")
marte = Planeta("Marte")

print(brasil)
print(portugal)
print()
print(terra)
print(marte)
print()

print(terra.falar_nome())
print(marte.falar_nome())
