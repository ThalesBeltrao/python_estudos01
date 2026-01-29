from math import factorial

def executa(funcao, *args):
    return funcao(*args)


def soma(x, y):
    return x + y

mult = lambda x, y, z: (x * 2, y * 3, z *  4)
print(*mult(2, 2, 2), sep="\n")

somar = executa(lambda x, y: x + y,  2,  3)
print(somar)



