# Crie uma classe Somar que guarde um número inicial (passado no __init__)
# e, quando for chamada, some outro número a ele.



class DobraValor:
    def __init__(self, f):
        self.func = f

    def __call__(self, *args):
        return self.func(*args) * 2

@DobraValor
def soma(*args):
    return sum(args)


# Sem usar o __call_ e sim um decorador de metodo como ficaria ?






#print(soma(2, 3, 4, 8))

### Metodo de Intâncias

class Serv1:
    def __init__(self,nome, local="LocalHost",):
        self.local = local
        self.nome = nome
        self.conectado = False


    def conectar(self):
        self.conectado = True
        return f"{self.nome} conectado"

serv1 = Serv1("servidor_dados")
#print(serv1.conectar())


# Metodo de Classe

class Serv2:
    def __init__(self, user, localhost="Localhost"):
        self.local = localhost
        self.user = user
        self.conectado = False

    @classmethod
    def conectar(cls, user):
        config = cls(user=user)
        return config

serv2 = Serv2.conectar("Servidor_rede")
#print(serv2.user, "conectado")

# Exercicios Saldo Bancario

class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = int(saldo)
        self.lista = []

    def deposito(self, valor1):
        self.lista.append(valor1) # Guarda o valor depositado
        soma_deposito = sum(self.lista) # cria uma variavel para somar os valores guardados
        self.saldo += valor1 # adiciona o valor depositado ao saldo total
        return f' valor depositado: R${soma_deposito}'.strip() # retorna os valores somados


    def sacar(self, valor2):

        if self.saldo <= 0:
            print("Saldo Insuficiente")

        elif valor2 > self.saldo:
            return "Saldo Insuficiente"

        self.saldo -= valor2

        return f'Valor sacado: R${valor2}'

    def saldo_total(self):
        return f'Saldo total: R${self.saldo}'


c1 = Conta("Thales", 100)

# Classmethod
class Conta2:
    def __init__(self,user=None, saldo=100):
        self.saldo = saldo
        self.user = user

    @classmethod
    def criar_conta(cls, user):
        conta = cls(user=user)
        return conta

    @classmethod
    def retornar_saldo(cls, saldo=100):
        saldo = cls(saldo=100)
        return saldo.saldo


print(Conta2.criar_conta("Thales").user)
print(Conta2.retornar_saldo())















