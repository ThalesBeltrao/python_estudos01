"""class Cachorro:
     def __init__(self, raça, peso ): # no começo é interessante voce passar os parametros para a classe
         self.raça = raça
         self.peso = peso


cachorro = Cachorro("Pastor Alemão",50)

#print(cachorro) # se eu não passo  os atributos da classe para a varivel cachorro ela mostra o lugar e que foi guardado
#print(cachorro.raça, end=" ")
#print(cachorro.peso) # ate agora só vimos atributos os quais são apenas qualidades da sua classe
# vamos aprender agora a como introduzir metodos em sua classe

#passando o atributo direto na classe


#class Cachorro2:
   # peso = 50 # eu eestou atribuindo uma instancia em uma classe isso quer dizer que todos os cachorros terão 50kg
    #def __init__(self,raça, cor):
       # self.raça = raça
       # self.cor = cor


#cachorro2 = Cachorro2("Labrador", "Preto")
#print(cachorro2.peso)
#print(Cachorro2.peso) # nesse caso posso mostrar a classe direto na funcao print


#Estado de Class
class Carro:
    def __init__(self, nome, ligando=False):
        self.nome = nome
        self.ligando = ligando

    def ligar(self):
        if self.ligando:
            print("{} Ja esta Ligado".format(self.nome))
            return

        print("{} ligado".format(self.nome))
        self.ligando = True

    def delisgar(self):
        if self.ligando:
            print("Desligando...")

        self.ligando = False
        print("{} desligado".format(self.nome))

    def acelerar(self):
        if not self.ligando:
            print("{} desligado, ligue para acelerar".format(self.nome))
            return

        else:
            print("{} Acelerando".format(self.nome))"""


# adicionadar metodos a classe

#class User:
    #def __init__(self,nome, senha):
        #self.nome = nome
        #self.senha = senha

    #@classmethod
    #def password(cls, nome):
        #return cls(nome, 123)


#user = User.password("thales")
#print(user.senha)
#print(user.nome)

class Carro:
    def __init__(self, nome, ligando=False):
        self.nome = nome
        self.ligando = ligando


    def ligar(self):
        if self.ligando:
            print("{} Ja esta Ligado".format(self.nome))
            return

        print("{} ligado".format(self.nome))
        self.ligando = True

    def delisgar(self):
        if self.ligando:
            print("Desligando...")

        self.ligando = False
        print("{} desligado".format(self.nome))


    def acelerar(self):
        if not self.ligando:
            print("{} desligado, ligue para acelerar".format(self.nome))
            return

        else:
            print("{} Acelerando".format(self.nome))

    def freiar(self):
        if self.acelerar:
            print("{} freiando".format(self.nome))
            return
        else:
            print("desligado ou ligado, acelere para freiar")



carro = Carro("Alpha Romeo")
