# criando uma classe
# primeiro voce passa a class e o nome com PascalCase
# depois passa o def e o __init
# () dentro precisa ir o self e depois os outros parametros
# sempre que for definizr uma instância voce precisa passar o self primeiro
#class é um molde para fazer classes como se fosse uma forma
class Carro:
    def __init__(self, nome):
        self.nome = nome
    def acecelar(self):
        print(f"{self.nome} esta acelerando...") # porque que executa direto o fusca. acelerando porque o print é um metodo(Açõ) por isso passa direto

fusca = Carro("thales".capitalize())
#print(fusca.nome)
#fusca.acecelar()

Carro.acecelar(fusca) # nesse caso a classe Carro esta executando um metodo direto, passando a variavel fusca