
#Introdução as Generator Functions em Pythpn
# generator = (n for n in range(1000)


def gerador(n=0):
    valor1 = int(input("Digite um valor: "))
    valor2 = int(input("Digite um valor: "))
    resultado = valor1 + valor2
    if resultado == 3:
        print("valor certo")

    yield resultado
    yield 3 + 6   # ele retorna esse valor e tem a capacidade de pausar funções diferentemente do return que executa e encerra
    return "Acabou"


gen = gerador(n=0)
print(next(gen))
print(next(gen))
print(gen.__iter__()) # mostra onde ele esta na memoria
print(iter(gen)) # mostra onde ele esta na memoria


#def funcao_pause(n=0):
    #yield 1  # chama a primeiro elemento da funcao por vez cada vez que voce chamar o next
    #print("continuando...")
    #yield 2
    #print("continuando...")
    #yield 3
    #print("vou terminar ")


#gen = funcao_pause()
#print(next(gen))  # nesse caso ele chama um elemento da funcao por vez cada vez que voce executa a funcao diferente do return que executa tudo sem pausa e encerra
#print(next(gen))
#print(next(gen))

#for i in gen:
   # print(i)

#print()

#def generator(n=0, maximum=10): # voce não precisa declarar o valor na sua variavel ou quando for chamar a funcao porque ela é posicional
    #while True:
       # yield n
       # n += 1 # somátorio

       # if n >= maximum:
         #   return

#gen2  = generator(2,8)
#for n in gen2:
    #print(n)


# yield from

#def gen1():
    #yield 1
    #yield 2
    #yield 3

#def gen2():
    #yield from gen1()  #você pode chamar uma outra funçao para ela executar junto com a sua funcao pause yield

    #yield 4
   # yield 5
   # yield 6


#num = gen2()

#for i in num:
  #  print(i)

# modulo 2 passando um parameetro para dentro da funcao
#print()


def gen1(): # apenas chama a funçao com next porque ela esta pausada executa uma por vez
    yield 1
    yield 2
    yield 3



def gen2(gen1):
    yield from gen1()
    yield 4
    yield 5
    yield 7


g = gen2(gen1)

for numero in g:
    print(numero)
