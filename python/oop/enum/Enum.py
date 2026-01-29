# Enum -> Enumerações
# Enumerações na programação, são usadas em benefícios onde temos
# um determinado número de coisas para escolher.
# Enums têm membros e seus valores são constantes.
# Enums em python:
# - são um conjunto de nomes simbólicos (membros) ligados a valores únicos
# - ser iterado para retornar seus membros canônicos na ordem de poder
# definição
# enum.Enum é uma superclasse para suas enumerações. Mas também pode ser usado
# diretamente (mesmo assim, Enums não são classes normais em Python).
# Você poderá usar seu Enum com type annotations, com isinstance e
# outras coisas relacionadas com tipo.
# Para obter os dados:
# membro = Classe(valor), Classe['usuario']
# usuario = Classe.usuario.name
# valor = Classe.usuario.valor

import enum

#Direcoes = enum.Enum("Direcoes", ["ESQUERDA", "DIREITA"])


class Direcoes(enum.Enum):
    ESQUERDA = 1
    DIREITA = 2


def mover(direcao:Direcoes):
    if not isinstance(direcao, Direcoes):
        raise ValueError("Direção não encontrada")
    print(f"movendo para {direcao}")


print(Direcoes.DIREITA.value)
mover(Direcoes.DIREITA)
#mover(Direcoes(1).value)

for i in Direcoes:
    print(i.value, i.name)


#enum.auto ela inumera sua variavel de maneira automatica