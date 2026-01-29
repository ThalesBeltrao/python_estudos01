# import sys

# print(sys.platform)

# Quando você for pegar algum modulo da bibliotéca tem que tomar cuidado com o nome da variavel

# Exemplo

# from sys import exit, platform

# Caso eu de um nome de platform para alguma variável ela sobreescreve meu modulo

# por isso tomar cuidado quando importar de maneira individual
# platform = ('oi')
# print(platform)

# tem como você pode renomar ou apelidar com o as

# from sys import platform as pt, exit as ex

# print(pt)

# importar tudo do modulo usando *
# má pratica deixa eu programa pesado porque importa toda a bibliotéca que tu nem usa
# from pandas import *


# Modularização do Código
# Entendendo os seus próprios módulos  Python
# O primeiro modulo executado chama-se __main__
# Você poe importar outro modulo inteiro ou parte do módulo
# O python conhece as pastas onde o __main__ está e as pastas a baixo dele
# Ele conhece pastar e módulos acima do __main__ por padrãp
# O python conhece todos os módulos e pacotes presentes
# os caminhos de sys.path

# import modulo_0
# import sys

# print("Este módulo se chama:", __name__)
# print(*sys.path, sep="\n")

try:
    import sys
    sys.path.append("C:/Users/thale/PycharmProjects/datascience/manip.arq")
except ModuleNotFoundError:
    print("Caminho não existe")

# Que loucura
import modulo_m01