#funções recursivas e recursividade
#funcoes que podem se chamar de volta
#uteis p dividir problemas grandes em partes menores
#toda funcao recursiva deve ter:
#um problema que possa ser dividido em partes menores
#um caso recursivo que resolve o pequeno problema
#um caso base que para a recursão
# fatorial - n! =5! = 5*4*3*2*1 = 120



def fatorial(n):
    if n == 0 or n == 1:
        return 1

    else:
        return n * fatorial(n-1)

print(fatorial(5))


def somar_lista(lista):
    if not lista:
        return 0

    return lista[0] + somar_lista(lista[1:])


lista = [2,2, 3, 4]
print(lista[1:])
print(somar_lista(lista))