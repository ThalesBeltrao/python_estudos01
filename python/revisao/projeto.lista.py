perguntas = [
    {"Pergunta": "Quanto é 2 + 2",
     "Opções": ["1", "3", "4", "5"],
     "Resposta": 4},
    {"Pergunta": "Quanto é 5 * 5",
     "Opções": ["25", "50", "30", "10"],
     "Resposta": 25}
]


def pergunta1():
    print(perguntas[0]["Pergunta"])
    for i, valor in enumerate(perguntas[0]["Opções"]):
        print("{}) {}".format(i, valor))

    def responder():
        while True: # vai ficar nesse ciclo ate colocar  o valor certo
            try:
                valor1 = int(input("Digite o a resposta: "))
                return valor1
            except ValueError:
                print("Digite os valores das opções")
    return responder


def pergunta2():
    print(perguntas[1]["Pergunta"])
    for i, valor in enumerate(perguntas[1]["Opções"]):
        print("{}) {}".format(i, valor))

    def responder():
        while True:
            try:
                valor2 = int(input("Digite o a resposta: "))
                return valor2
            except ValueError:
                print("Digite as opções")
    return responder


while True:
    resposta = pergunta1()
    if resposta() == perguntas[0]["Resposta"]:
        print("Certo")
        continuar = input("Deseja ir para a proxima [S] [N]: ").strip().lower() # por eu tirar o espaço e converter tudo para minusculo não importa se sera M ou n

        if continuar == "s":  # or continuar == "S":
            resposta2 = pergunta2()
            if resposta2() == perguntas[1]["Resposta"]:
                print("Certo")
                break

            elif resposta != perguntas[0]["Resposta"]:
                print("Errou !")
                tentar_de_novo = input("Quer tenter de novo [S] [N]: ").strip().lower()

                if tentar_de_novo == "s": #or tentar_de_novo == "S":
                    ...
                elif tentar_de_novo == "n": #or tentar_de_novo == "N":
                    break



    elif resposta != perguntas[0]["Resposta"]:
        print("Errou !")
        tentar_de_novo = input("Quer tenter de novo [S] [N]: ").strip().lower()

        if tentar_de_novo == "s": # or tentar_de_novo == "S":
            continue
        elif tentar_de_novo == "n": # or tentar_de_novo == "N":
            print("Proxima pergunta ")

            resposta2 = pergunta2()
            if resposta2() == perguntas[1]["Resposta"]:
                print("Certo")
                break

            elif resposta != perguntas[0]["Resposta"]:
                print("Errou !")
                tentar_de_novo = input("Quer tenter de novo [S] [N]: ").strip().lower()

                if tentar_de_novo == "s": #or tentar_de_novo == "S":
                    ...
                elif tentar_de_novo == "n": # or tentar_de_novo == "N":
                    break



