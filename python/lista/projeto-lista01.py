

lista = []
contador = 0
while True:
    print("selecione uma opção ")
    opcao = input("i(inserir), a(apagar), l(listar), s(sair): ")
    if opcao == "i":
        nome = input("coloque seu nome: ")
        cpf = input("coloque seu cpf: ")
        idade = input("coloce sua idade: ")
        endereco = input("coloque seu endereço: ")
        cep = int(input("coloque seu cep: "))
        lista.append(nome) # nesse caso os elementos da variaveis que vai passado ela vai para a lista vazia
        lista.append(cpf)
        lista.append(idade)
        lista.append(endereco)
        lista.append(cep)

    elif opcao == "a":
        print("a")
        indice_str = input("Qual indice voce quer Apagar: ")

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print("Porfavor digite um numero inteiro")

        except IndexError:
            print("Indice não consta na lista")




    elif opcao == "l":
        if len(lista) == 0:
            print("lista vazia")
        elif len(lista) > 0:
            for i in enumerate(lista):
                print(i)
                print()
            print(lista)

        elif opcao == "s":
            print("Voce saiu do cadastro")
            break



