

def tabuada(valor_fixo):
    def passe_valor(valores):
        multiplica = valor_fixo * valores
        return multiplica

    return passe_valor


tabuada_2 = tabuada(4)

for i in range(1, 11):
    print(tabuada_2(i))
print()

# funções recursivas
def executa(func):
    print("vou te decorar")

    def interna(*args, **kwargs):
        for i in args:
            isint(i)

        resultado = func(*args, **kwargs)

        print("o seu resultado foi {}".format(resultado))

        return resultado

    return interna


@executa
def soma(x, y):

    return x + y



def isint(param):
    if not isinstance(param, int):
        raise "não é um inteiro"


somar = soma(2, 10)
print(somar)


