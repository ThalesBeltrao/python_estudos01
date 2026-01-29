"""Interpolação de strings
%s para strings
%d  e %i para string
%f para float
x e X para hexadecimal(ABCDEF0123456789)
"""

nome = "luiz"
preco = 1000.95897643
variavel ="%s, o preço é R$%f " %(nome, preco)
print(variavel)
