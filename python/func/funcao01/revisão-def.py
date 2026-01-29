# funcao
# argumentos o que vai ser executado quando chamar a funcao
# parametro o que voce passa dentro da funcao


#def soma(n, m): # eu estou passando um parametro para eles porem não é posicional nesse caso eu tenho que passar no argumento da funcao quando keu for chama-lo
    #print(n + m)

#soma(2, 3)  argumento note que temos 2 argumentos, caso eu passe mais um vai gerar um erro


def criar_saudacao(saudacao, nome):
    return f"{saudacao},{nome}"


def executa(funcao, *args): # uma funcao que executa outras funções
    return funcao(*args)


print(executa(criar_saudacao,"bom dia", "thales"))
print()

def criar_saudacao(saudacao, nome):
     def saudar():
         return f"{saudacao},{nome}"
      #return saudar() nesse caso a funcao ela esta sendo chamada pelo return para ser executada voce pode passar ela em um print
     return saudar



saudacao = criar_saudacao("bom dia", "julia") # é como essa variavel fosse uma funcao
print(saudacao())
print(criar_saudacao("boa noite", "thales")) # como ela esta guardada na memoria e eu não executei ela no return ela precisa ser passada a uma variavel

# deixando a funcao mais dinamica

def criando_fala(fala1="boa noite",fala2="bom dia"):
    def pessoa(nome):
        return f"{fala1},{nome}" # ele vai retornar o parametro da funcao primaria e depois da funcao secundária

    return pessoa


fala_bomdia = criando_fala("bom dia")
fala_boaboite = criando_fala()
print()
#print(fala_boaboite("thales"))

for nome in ["thales","julia", "augusto"]:
    print(fala_boaboite(nome))
