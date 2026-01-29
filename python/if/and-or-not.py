
# Operadores Lógicos
# and(E), Or(ou) Not(não)
# Verdadeiras
# se qualquer valor for considerado falso
# 0, 0.0, "" é False
# None é False  Representado como um não valor


#entrada = input("[E]ntrar [S]air: ")
#senha_digitada = input("Senha:")

#senha_permitida = "123456"

#if entrada == "E" and senha_permitida == senha_digitada: # As duas condições precisam ser verdadeiras se não ele pula para o else
    #print("Entrar")

#else:
   # print("Sair")

#print()

#Avaliação de curto circuito
#print(True and True and True) #and todas tem que ser verdadeiro se não ele pula para outra condição no if"""

# or As duas condições precisam ser verdadeiras se não ele pula para o else

"""entrada = input("[E]ntrar [S]air: ")
senha_digitada = input("Senha:")

senha_permitida = "123456"

if (entrada == "E" or entrada =="e") and senha_permitida == senha_digitada: # nesse caso voce coloca entre parentese para dar prioridade na checagem
    print("Entrar")

else:
    print("Sair")

print()"""


""""# curto circuito
print(True or False)
print()
print(0 or False or 0 or "abc" or  True)
senha = input("senha: ") or "sem senha"
print(senha)"""


#not inverter expressão
#not True = False
#not False = True


#senha = input("senha: ")

#if not senha:
    # print("você não digitou nada") # se não senha se voce não colocar nada ele vira True e executa o comando de baixo o print

"""entrar = input("Digite E[ntrar] ou S[air]: ")
entrada = "E"
senha = "123456"
saida = "S"

if entrar == "e" or entrar == "E":
    print("Você entrou no sistema ")
    colocar_senha = input("Digite sua senha: ")
    if colocar_senha == senha:
        print("Sua senha esta efetivada")
    else:
        print("Esta com erro de acesso")

elif entrar == saida:
print("Você saiu") """

senha = input("Digite sua senha: ") or "sem senha"
print(senha)