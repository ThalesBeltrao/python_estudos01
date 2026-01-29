# Try, Except, Else e Finally
# tratamento de erros

a = 8
b = 0
c = a/b
try:
   a = 8
   b = 0
   print("linha 1")
   c = a/b # silenciar um erro não é uma boa pratica quando voce não trata esse erro
   print("linha 2") # não é executado por que o erro voce pula para excepet
except ZeroDivisionError:
    print("Dividiu por 0")
except NameError: # aqui pode tratar mais de um erro diferente apenas chamando um try e varios erros
    print("o nome da variavel não esta definida")
except Exception:
    print("preste atenção no seu codigo idiota") # essa é a maior classe de erro que temos dentro do python
except(TypeError, IndexError): # nesse caso aqui aida pe possível passar dois tipos de erros sumultaneos para o except
        ...
print("Continuar")



# try e finally

try:
    print("abrir arquivo")
    8/0
finally:
    print("fechar arquivo") # finally mesmo com o erro ele é executado mostrando seu arquivo


# raise lançando exceções

def divide(a, b):
    try:
        return a/ b
    except ZeroDivisionError:
        raise # relançar um erro

print(divide(8,0))



def divide(n, d):


    if d == 0:
        raise ZeroDivisionError("valor dividido por 0")
    return n / d


#print(divide(8, 0))"""


"""def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError("d não pode ser 0")



def int_float(n):
    if not isinstance(n, (float, int)):
        raise TypeError("não aceita letras")


def divide(n, d):
    int_float(n)
    int_float(d)

    nao_aceito_zero(d)
    return n / d

print(divide(8, 9))"""
