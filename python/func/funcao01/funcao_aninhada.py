# Criar uma função que executa outra função
def soma(x, y):
   print("Executei soma")
   return x + y


def executa(funcao, x):
    print("Executei executa")

    def interna(y):
        print("Exceutei ")
        return funcao(x, y)
    return interna


executar = executa(soma, 2)
print(executar(4))


# Função com parametro None
def somar(x, y, z=None):
    if z is not None:
        print(x + y + z)
    else:
        print(x + y)

#somar(2, 3, 6)

################################################

def adicionar_item(item, lista=None):
    if lista is None:
        lista = []
    lista.append(item)
    return lista


lista01 = adicionar_item(["maça","banana", "abacate"])

print(*lista01)

# Exemplo de Bugs Ocultos


def pegar_lista(lista=[]):
    def gravar_dados(item):
        lista.append(item)
        return lista
    return gravar_dados


salvar01= pegar_lista()
salvar02 = pegar_lista()

salvar01("a")
salvar02("b")
salvar01("c")

print(salvar01("y"))
print(salvar02("x"))

# Se você não passa uma lista dentro da função ela reutiliza e armazena todos os dados
# De todas as variáveis na mesma lista da função, por mais que seja variávies diferentes
print()
# Função com "Histórico embutido"
def historico(item, lista=[]):
    lista.append(item)
    return lista


print(historico("A"))
print(historico("B"))
print(historico("C"))
print()

# Usando o None

def pegar_lista(lista1=None):
    if lista1 is None:
        lista1 = []

    def pegar_item(item):
        lista1.append(item)
        return lista1
    return pegar_item


listando1 = pegar_lista()
listando1("A")
listando1("C")
print(listando1("B"))
print()

listando02 = pegar_lista()
listando02(3)
listando02(4)
print(listando02(5))




### Exemplo de conectividade entre as portas

def conetar(servidor, porta=None):
    if porta is None:
        porta = 3336
        print(f"{servidor} está conectado na porta {porta}")

    else:
        print(f"{servidor} está conectado na porta {porta}")


conetar("AWS",1800)