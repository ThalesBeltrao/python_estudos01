"""
fazer um programa que o usuario digite um numero inteiro e ele verifica se é par ou impar
caso ele não digite um numero inteiro , informe que ele não digitou um numero inteiro

"""
try:
    numero = int(input("Digite um numero inteiro:"))
    numero_par = numero % 2

    if numero_par == 0:
        print("Numero é par")
    else:
        print("Numero é impar")
except:
    print("Você não digitou um numero Inteiro")

