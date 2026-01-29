# operação ternária (condicional de uma linha)
# <valor> if <condição> else <outro valor >

variavel = 10 if True else 0
print(variavel)

idade = 20

status = "Adulto" if idade >= 18 else "Criança"
print(status)



lista = [10, 20, 30]
resultado = [meta for meta in lista if meta >= 20]
soma = list(map(lambda x: x * 2, resultado))
print(resultado)
print(soma)