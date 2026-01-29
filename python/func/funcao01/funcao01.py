import random


# função com parametros

def valor(a, b, c):
    print(a, b, c, sep="\n")

n1 = "thales"
n2 = "bruna"
n3 = "vanessa"

#valor(n1, n2, n3)

# Argumento nomeado sinal de igual

#def soma(x, y, z=None): # defino None porque fica ao meu critério somar z ou não
    #if z is not None:
       # print(x + y + z)

    #else:
       # print(x+y)

#soma(2,5, 10)

# Escopo da função onde ela pode ser acessada

x = 10

def executar():
    x = 11
    def outra_funcao():

        x = 12
        y = 9
        print(x, y, sep="\n")
    outra_funcao()
    print(x) # Esse x faz referência a variável de função principal, ela não tem acesso a função ineterna

executar()

# Exercicios

# 1- Criar função saudar com dois parametros um None = periodo
# 2- Criar uma função com nome e sua permissão(user, adm, etc)
# 3- Criar uma função com verificaçao a senha se é fraca ou não

caracteres = [chr(i) for i in range(33, 127)]
senha_fraca = random.sample(caracteres, 6)
senha = "".join(senha_fraca)

caracteres = [chr(i) for i in range(33, 127)]
senha_forte = random.sample(caracteres, 12)
senha1 = "".join(senha_forte)



def analisador_senha(analisar=None):
    if  analisar is None:
        print(f"senha fraca: {senha}")

    else:
        print(f"senha forte: {senha1}")

analisador_senha(senha1)