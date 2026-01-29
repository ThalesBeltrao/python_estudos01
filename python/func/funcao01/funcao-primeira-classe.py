"""Higher Order Funcions"""

def saudacao(msg, nome): # quando tem dois ou mais parametros ela pode ser uma tupla ou um dicionario
    return f"{msg}, {nome}"



def executa(funcao, *args):
    return funcao(*args)



print(executa(saudacao, "bom dia","thales"))
print()

#clousure e funções que retornam outras funções

def criar_saudacao (saudacao, nome):
    def saudar():
        return f"{saudacao},{nome}"

    return saudar #() quando a funcao é executada  bloco de baixo quando não chama a funcao ele salva na memoria e voce pode passar a executar ela direto na variavel

s1 = criar_saudacao("bom dia", "thales")
s2 = criar_saudacao("boa noite", "bruna")
print(s1()) # () se eu não executo o valor de funcao ela vai aparecer o lugar do armazenamento
print(s2()) # nesse caso o return saudar não esta sendo executado então ele guarda o valor na memoria para ser executado em uma variavel


# deixando mais dinamico o código


def criar_fala(fala):
    def pessoa(nome):
        return f"{fala},{nome}"
    return pessoa # esta guardada na memoria precisa ser colocada em uma variavel para essa variavel virar uma funcao e voce executala dentro de um print

falar_bomdia = criar_fala(" Bom dia")
falar_boanoite = criar_fala(" Boa noite")

print(falar_bomdia("luiz".capitalize()))
print()

for nome in ["Thales", "Fernando","Gabriel"]:
    print(falar_boanoite(nome))


# Criar Funções que duplicam, triplicam e quadruplicam
#o numero recebito

def criar_multiplicador(multiplicador): # aqui eu crei uma funcao com um valor variavel posso passar qualquer valor para a variavel

    def multiplicar(numero): #crie outra funcao que nesse caso eu vou passar um numero de dentro de uma variavel quando chamar o print
        return numero * multiplicador
    return multiplicar # nesse caso ele salva o valor na memoria para usar depois em uma string

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quaduplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quaduplicar(2))

