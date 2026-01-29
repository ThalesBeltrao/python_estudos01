# tru, except, else finaly
a = 18
b = 0
try:
    c = a/b
except ZeroDivisionError:
    print("Esta tantando dividir por 0")


except NameError:
    print("Sua variável não esta definida")

print("Continuar")
print()
# se voce não passa a execeção para o except
# O que ocorre que qualquer outro erro vai se enquadrar no excep

try:
    a = sum([2], [3])
    print(a)
except TypeError:
    print("A funcao {sum} não concatena listas, apenas soma valores dentro da lista")
except Exception: # O Exception ele trata qualquer tipo de erro
    print("Erro descomnhecido")
print()

# Trabalhar com dois erros no except como uma tupla
# Não faz muito sentido

d = 3
e = "a"

try:
    f = e/a
    g = f[0]
except (TypeError, NameError) as erro:
    print("Tipo do erro foi:", erro.__class__.__name__ )


# Finally e Else
# O finally sempre será executado mesmo que ocorra um erro
# Geralmente usado para fechar conexões
# pode ser usados com o except tambem

try:
    ...
finally:
    ...

# Try, except, finally
try:
    ...

except:
    ...

finally:
    ...

