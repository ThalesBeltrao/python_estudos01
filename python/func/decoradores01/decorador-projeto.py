# criar uma funcao que soma um número
# Depois é Decorado e aplica a raiz quadrada
from math import sqrt


def decorador_valor(func):
    def interna(*args):
        # valor recebido da execução da funcao soma
        valor = func(*args)

        # Valor modificado
        modify = sqrt(valor)

        return f"Esse é o valor recebido {valor} da funcao: {func.__name__}, Esse o valor modificado {modify}"
    return interna


@decorador_valor
def soma(x, y):
    return x * y



print(soma(5, 5))