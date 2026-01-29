lista = []
listagem = [lista]
count = 0
while count < 4:

    if count > 3:
        break
    print("Faça seu cadastro")
    nome = input("Digite seu nome:").capitalize()
    count += 1
    if nome.isnumeric():
        print("Coloque seu nome")

    try:
        idade = int(input("Digite sua idade:"))
    except ValueError:
        input("Didite sua idade: ")

    def cadastro_cpfs():
        cpf_enviado = input("Digite seu cpf:")
            #.replace(".","")\
            #.replace(".","")\
            #.replace("-","")\

        nove_digitos = cpf_enviado[:9]
        contador_regressivo_1 = 10
        resultado_1 = 0
        for digito in nove_digitos:
            resultado_1 += int(digito) * contador_regressivo_1
            contador_regressivo_1 -= 1

        digito_1 = ((resultado_1 * 10) % 11)
        digito_1 = digito_1 if digito_1 <= 9 else 0



        #segunda perte
        dez_digitos = nove_digitos + str(digito_1)
        contador_regressivo_2 = 11

        resultado_digito_2 = 0
        for digito in dez_digitos:
            resultado_digito_2 += int(digito) * contador_regressivo_2
            contador_regressivo_2 -= 1

        digito_2 = (resultado_digito_2 * 10) % 11
        digito_2 = digito_2 if digito_2 <= 9 else 0


        cpf_gerado = f"{nove_digitos}{digito_1}{digito_2}"

        if cpf_enviado == cpf_gerado:
                print(f"{cpf_enviado} é valido")
        else:
            print("cpf invalido")
            return





    cep = input("Digite seu cep:")

    lista.append(nome)
    lista.append(idade)
    lista.append(cadastro_cpfs)
    lista.append(cep)


    break




print(*lista)






