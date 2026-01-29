#Métodos em instâncias d eclasses Python
class Car:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f"{self.nome} esta acelerando...") # metodo dentro da classe e uma instancia é uma ação


fusca = Car("fusca".capitalize())
print(fusca.nome)
print()
celta = Car(nome="Celta")
print(celta.nome)

fusca.acelerar()# como se fosse chamar uma funcao de dentro de uma variavel
