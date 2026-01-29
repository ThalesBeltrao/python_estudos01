# Variáveis livres + nonlocal

def fora():
    a = 1 # variável livre
    def dentro():
        return a # Porque não está definida como parametro da funcao
    return dentro


def concatenar(string_inicial):
    values_finily = string_inicial
    # A funcao interna não consegue alterar o valor values_finily
    # Por que ela é livre
    # Para haver alteração do valor e poder usar ela na funcao interna
    # deve se passar nonlocal nome_da_variável
    # Dessa maneira você consegue acessar o valor dela

    def interna(valor_concatenar):
        nonlocal  values_finily
        values_finily += valor_concatenar
        return values_finily
        # UnboundLocalError vai gerar esse erro porque a funcao não é local
    return interna



#c = concatenar("a")
#(c("B"))



# Nonlocal ele serve para que a variável da funcao principal seja alterada
# Exemplo


def contador():
    contador = 0

    def interna(valor):
        nonlocal contador
        contador += valor
        return f"Estou sendo modificado: {contador}"

    return interna




contar = contador()
#print(contar(1))
#print(contar(1))
#print(contar(1))


# fazendo um nonlocal
# Modificando com valores mutáveis como uma lista ou um dicionário

def modify_dict():
    dicionary = {"Valor": 0}
    print(dicionary.items())

    def interna(incremento):
        nonlocal dicionary
        dicionary["Valor"] += incremento
        return f"Valor da funcao primaria modificada: {dicionary["Valor"]}"
    return interna



