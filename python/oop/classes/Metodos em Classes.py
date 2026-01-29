# Mètodos de classe
# são metodos onde "self sera "cls ou seja
# ao inves de receber a intancia primeiro
# parametro recebemos a propria classe


class Pessoa:
    ano = 2023 # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod # esta passando a classe direto na funcao
    def metodo_de_classe(cls):
        print("hey")


p1 = Pessoa("João", 34)
#print(Pessoa.ano)
Pessoa.metodo_de_classe(p1) #precisa passar a variavel que esta com os atirbutos da classe Pessoa

print()
# tem como voce usar uma funcao chamando direto da classe sem precissar passar argumento
# @classmethod


class Pessoa2:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    @classmethod    # isso faz com que voce não passe parametros quando for chamar uma funcao na classe
    def metodo_classe(cls, nome):
        return cls(nome, 50)



p2 = Pessoa2("Thales", 32)
p3 = Pessoa2.metodo_classe("junior")
#print(p2.nome, p2.idade)
#print(p3.nome, p3.idade)  #  nesse caso chama-se o a funçao de dentro do metodo direto na classe sem precisar jogar ela em uma variavel chamar a variavel chamar a funcao e depois passar o argumento


