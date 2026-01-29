# Faça uma lista de compra com listas
# O usuario deve ter a possibilidade de
# inserir, apaga e listar valores da sua lista
# não permita que o programa quebre com erro de indices inexistente na lista
lista = []

while True:

    menu = input("[sair], [adicionar], [deletar], [listar]: ")

    if menu == "sair":
      print("voce saiu da lista")
      break

    elif menu == "adicionar":
        add_fruta = input("Adicione sua fruta: ")


        lista.append(add_fruta)

    elif menu == "listar":
        if not lista:
            print("Adicione elemento a lista")
        for i in enumerate(lista):
            print(i)

        print()

    elif menu == "deletar":
        if lista:
            try:
                index = int(input("Digite  o indice que deseja deletar: "))
                lista.pop(index)
                print("Fruta removida pelo indice")

            except ValueError:
                print("Digite um numero inteiro")

            except IndexError:
                print("Indice não existe")


# quando voce coloca uma lista dentro do while, vazia toda vez que voce coloca um valor nela ela sobreescreve o valor
# para corrigir esse problema você deve fazer uma lista fora do while dessa