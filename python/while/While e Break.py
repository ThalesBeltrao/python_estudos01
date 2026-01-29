
#Repetições
#while (enquanto
#Executa uma ação enquanto uma condição fo verdadeira

"""condicao = True

contador = 0

while condicao:
    contador = contador + 1
    nome = (input("Digite seu nome: "))

    if nome == "sair":
        print("Você saiu")
        break  # nesse caso o break depois de atingir certa condição ele quebra o laço e sai do while dando continuidade ao programa


#digite_seu_cpf = input("Digite seu cpf: ")"""


'''Operadores de Atribuição 
= += -= *= /= //* **= %='''



"""contador = 0

while contador < 10:
    contador = contador + 1
    print(contador)"""


#print("Acabou")


# continue pular laços

#contador = 0

#while contador < 50:
    #contador += 1

   # if contador == 6:
       # continue # pulou o 6
    #print(contador)

    #if contador == 30:
       # break

"""qtd_linhas = 5
qts_colunas = 5

linha = 1

while linha <= qtd_linhas:
    coluna = 1

    while coluna <= qts_colunas:
        print(f"{linha=}, {coluna=}")
        coluna += 1
    linha += 1


print("acabou")"""

# decoradores01 calculadora
#  1-)fazer o input de dois valores
#  2-)mostrar a opção da calculadora
#  3-)efetuar o resultado


"""while True:
    resultado_1 = int(input("Digite um valor:"))
    resultado_2 = int(input("Digite um valor:"))

    execucao_valor = input("O que voce quer fazer? somar, subtracao, multiplicacao:")
    soma = resultado_1 + resultado_2
    subtracao = resultado_1 - resultado_2
    multiplicacao = resultado_1 * resultado_2

    if execucao_valor == "somar":
        print(soma)

    elif execucao_valor == "subtracao":
        if resultado_1 < resultado_2:
            print(resultado_2 - resultado_1)

        elif resultado_1 > resultado_2:
            print(subtracao)
    elif execucao_valor == "multiplicacao":
        print(multiplicacao)
    if execucao_valor == "sair":
        break"""

"""while True:
    sair = input("Quer sair?sair ou não: ").lower().startswith("s")

    if sair is True:
        break"""

while True:
    numero_1 = input("Didite um numero: ")
    numero_2 = input("Didite um numero: ")
    operador = input("Didite um operador (-),(+),(*): ")
    operadores_validos = "-+*"


    numeros_validos = None
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)

        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print("Os numeros não são validos")
        continue

        operadores_validos = "-+*"

    if operador not in operadores_validos:
        print("Operador invalido")

    if len(operador) > 1:
        print("Apenas um operador")
        continue

    sair = input("Quer sair? sim ou não: ").lower().startswith("s") # começa com ele deixa o numero boleado

    if sair == True:
        break
