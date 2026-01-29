# mantendo Estado dentro da classe

class Camera:
    def __init__(self,nome, filmando = False, fotografando= False, bateria = 100):
        self.nome = nome
        self.filmando = filmando
        self.fotografando = fotografando
        self.bateria = bateria
    # Atribudos de um Classe são suas caracteristicas

    def filmar(self): # metodo são ações que as classes tem e podem ser chamadas pelas instãncias
        if self.filmando:
            print(f"{self.nome} já está filmando...")
            return

        self.filmando = True
        print(f"{self.nome} filmando...")
        self.bateria -= 10


    def parar_filmagem(self):
        if not self.filmando:
            print(f"{self.nome} não esta filmando...")
            return
        self.filmando = False
        print(f"{self.nome} parando de filmar...")

    def check_bateria(self):
        print(self.bateria)

    def carregar_bateria(self):
        if self.bateria == 100:
            print("Bateria com 100% de carga")
            return
        self.bateria += 10


c1 = Camera("Sony")
c1.filmar()
c1.parar_filmagem()
c1.parar_filmagem()
c1.check_bateria()
c1.carregar_bateria()
c1.check_bateria()
c1.carregar_bateria()
c1.filmar()
