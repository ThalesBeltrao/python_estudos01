import re

#Contagem de Caracteres:
#Peça ao usuário uma frase e mostre quantos caracteres ela possui (com e sem espaços).

# quantidade com espaço
#frase = input("Digite um textto, uma frase: ")
#qtd_caracteres = len(frase)

#(f"{qtd_caracteres} caracteres contando espaços, pontos, acentos")

#quantidade sem espaço
#frase1 = input("Digite um textto, uma frase: ")
#qtd_caracteres_semespaço = len(frase.replace(" ", ""))

#(f"{qtd_caracteres_semespaço} caracteres contando pontos, acentos, sem espaços,")

#Caixa Alta e Baixa:
#Leia uma string e exiba:
#a) Em letras maiúsculas
#b) Em letras minúsculas
#c) Apenas a primeira letra em maiúsculo (capitalize)

nome = "thales willian"
#print(nome.lower()) # Minusculas
#print(nome.upper()) # Maisculas
#print(nome.capitalize()) # Primeira Maíscula se tiver dois nomes juntos não funciona Thales willian

#print(nome.title()) # Toda primeira letra maiscula Thales Wilian
#print(nome.strip()) # Retira todos os espaçoes esqueda e direita
#print(nome.strip()) # Retira todos os espaçoes esqueda e direita
#print(nome.swapcase()) # Inversão se estiver em Maiscula fica minuscula

cpf = input("Padrao[xxx.xxx.xxx-xx]: Digite seu cpf: ")

estruta = "xxx.xxx.xxx-xx"
contagem = len(estruta)
contagem_cpf = len(cpf)

if contagem != contagem_cpf:
    print("Fora dos padrões")