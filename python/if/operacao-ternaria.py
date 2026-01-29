"""
Operadores ternarios(condicional de uma linha
<Valor> if <condicao> else <outro valor>
"""
# Sintaxe
# True_value if teste else False_value

idade = 20
status = "Maior de idade " if idade >= 18 else "Menor de Idade"
print(status)

valor = int(input("Digite um numero: "))
verificacao = "Par" if valor % 2 == 0 else "Impar"
print(verificacao)

# Utilizando is e in no if ternário

