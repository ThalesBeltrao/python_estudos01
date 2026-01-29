class Carro:
    def __init__(self, cor, modelo, marca):
        self.cor = cor
        self.modelo = modelo
        self.marca = marca
    def acelerar(self):
        return f"{self.modelo} está acelerando..."



#car1 = Carro("Azul", "Focus", "Ford")
#print(car1.acelerar())


# Escopo dentro dos métodos da classe funcionam de forma interna
# Só tem acesso interno


class Animal:
    def __init__(self, nome):
        self.nome = nome
        variavel = "valor"
        print(variavel)

    def comendo(self, comer):
        return f"{self.nome} está comendo {comer}"

    # posso executar diversos atos chamando a função comendo passando args e kwargs
    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)

#leao = Animal("Simba")
#print(leao.executar(["maça", "banana"]))

# Colocando Estado nas Classes

class Camera:
    def __init__(self, modelo, filmando= False, ligado= False):
        self.modelo = modelo
        self.filmando = filmando
        self.ligado = ligado

    def ligar(self):
        if self.ligado:
            print(f"{self.modelo} ja está ligada")
            return

        self.ligado = True
        print(f"{self.modelo} camera ligada")

    def desligar(self):
        if not self.ligado:
            print(f"{...}")
            return
        self.ligado = False
        print(f"{self.modelo} desligado")

    def filmar(self):
        if self.ligado:
            print(f"{self.modelo} filmando...")
            return
        elif not self.ligado:
            print(f"{self.modelo} camera desligada...")
            return


c1 = Camera("Sony")
c1.ligar()
c1.desligar()
c1.filmar()
c1.ligar()
c1.filmar()
c1.desligar()
c1.filmar()

