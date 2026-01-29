# Classes decoradoras

class Multiplicar:
    def __init__(self, func):
        self.func = func
        self.multiplicador = 10

    def __call__(self, *args, **kwargs):
        resultado = self.func(*args, **kwargs)
        return resultado * self.multiplicador


@Multiplicar
def soma(x, y):
    return x + y


somar = soma(2, 4)
print(somar)

# segunda maneira executando a class na funçao



class Dividir:
    def __init__(self, divisor):
        self._divisor = divisor

    def __call__(self, func):
        def interna(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado // self._divisor

        return interna


@Dividir(2)
def somando(x, y):
    return x + y



dividindo = somando(2, 2)
print(dividindo)