"""Try/Except
try >>> tentar executar o codigo
execpt >> ocorreu algum erro ao tenter executar
"""

# print(456)
# try:
# int("a")
# except:
# print("não é um numero")

numero_str = input("Digite um numero e eu vou dobrar: ")

try:
    numero_float = float(numero_str)
    print(numero_float * 2)
except:
    print("Você não digitou um numero")
