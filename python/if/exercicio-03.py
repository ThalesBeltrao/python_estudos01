"""
Faça um programa que peça o primeiro nome do usuário, caso o nome tiver 4 letra ou menos escreve seu nome é curto,
se tiver entre 5 ou 6 letras, escreva seu nome é nomal, maior que 6escreva seu nome é muito grande
"""
nome = input("Digite sue nome: ")

contar_nome = len(nome)

print(f"seu nome tem {contar_nome} letras")

if contar_nome <= 4:
    print("seu nome é pequeno")
elif contar_nome == 5 or 6:
    print("Seu nome tem o tamanho normal")
elif contar_nome > 6:
    print("Seu nome é grande")
