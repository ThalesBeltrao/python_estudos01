"""Módulos padrão em python (import, from ,as , e * )
hhtps://docs.python.org/3/py-dodindex.html
inteiro - import nome_modulo
Vantagens voce tem o namespace do módulo
Desvantagens: nomes grandes



partes do modulo - from nome_modulo import objeto1, objeto2
Vantagens: voce tem os nomes pequenos
desvatagens: sem o nome space do módulo

alias1 - import nome_módulo as apelido = as é como voce quisese renomar algo
alias2- form nome_módulo import objeto1 as apelido
vantagens voce pode reservar nomes para o seu codigo
desvantagem pode ficar fora do padão em python


#má pratica - from nome_módulo import *
#vantagem importa tudo do modulo
# desvatagem importa tudo do módulo

import sys   # importando tudo do modulo
from math import sqrt #apenas um objeto do modulo

print(sys.platform) #importanto todo o modulo
print(sqrt(25)) # importanto apenas o objeto do modulo


#importado e mudando o nome do modulo com as
import sys as s
# agora o sys passa a ser s

# renomando objeto do módulo
from sys import exit as ex, platform as pf


print(pf)
ex()

#Modularização  
Entendendo seus proprios módulos Python
o primeiro modulo exdcutado chama-se __main__
voce pode importar outro modulo inteiro ou parte dele
o pyhthon conhece a pasta onde o __main__ esta
abaixo dele.
ele não conhece pastas e modulos acima do __main__
o python conhece todos os modulos e pacotes

import sys
#sys.path.
from modulo_m import soma# importando seu proprio modulo


print("este modulo se chama", __name__)
#print(*sys.path, sep="\n")
#print(modulo_m.variavel_a)

somar = soma(2,15)
print(somar)"""

# recarregar o modulo import importlib

#import importlib

#import modulo_m


#for i  in range(10):
 #importlib.reload(modulo_m)

#print(modulo.soma(2,3))
#print(Aula_package.modulo.soma(2,6))
#print(variavel)


#print(Aula_package.dobra(5))
import modulo_m
from modulo_m import fala_oi, soma


print("Esse modulo de chama", __name__)
modulo_m.fala_oi()

print(soma(3,5))

print()
fala_oi()


