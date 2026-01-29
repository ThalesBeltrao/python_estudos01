from decimal import Decimal

#numero_1 = 0.1
#numero_2 = 0.7
#numero3 = numero_1 + numero_2
#print(numero3)
#print(f"{numero3:.2f}")# ele arredonda para cima porem isso é uma string
#print(round(numero3, 2)) # segunda opção

# terceira maneira

numero_1 = Decimal("0.1")
numero_2 = Decimal("0.7")
numero3 = numero_1 + numero_2

print(numero3)