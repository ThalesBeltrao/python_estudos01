"""
# @property um getter no modo Pythonico
#getter- um metodo para obter ym atributo
#modo pythonico - modo do python fazer as coisas
#é um metodo que se comporta como um atributo
#Geralmente é usada nas seguintes situações
#como getter
#p/envitar quebra de codigo cliente
#para/habilitar setter
#p/ executar ações ao obter um atibuto"""


#class Caneta1:
    #def __init__(self, cor):
        #self.cor_tinta = cor
    #def get_cor(self):  # nesse caso é como o def get_cor ele fosse um funcao que altera seu codigo e todos os outros que utilizam ele

        #return self.cor_tinta




#caneta = Caneta1("Azul")
#print(caneta.get_cor())
#print(caneta.get_cor())
#print(caneta.get_cor())


#property ele funciona da mesma forma que um getter


#class Caneta:
    #def __init__(self, cor):
        #self.cor_tinta = cor # caso eu mude o nome da instancia aqui vai quebrar o programa de quem esta usando meu codigo então nesse caso pode se usar o metodo property


    #@property
    #def cor(self):
        #return self.cor_tinta


#c1 = Caneta("Azul")

#print(c1.cor) # perceba que ele mesmo sendo uma instacia com o nome diferente agora não quebra o código metodo executa uma ação ()

class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    def get_cor(self):
         return self.cor_tinta


# Exemplo caso ele use um atributo da classe e depois tenha que mudar pode quebrar o código
# Exemplo

cor = Caneta("Azul")
#print(cor.cor) # nesse caso se o atributo mudar de nome da problema em todas as váriáveis
print(cor.get_cor()) # nesse caso o get pega esse valor do atributo e voce não precisa quebrar o programa mudando o nome de todo
# Atributo que foi utilizado

# Uma outra maneira de ser utilizado seria usando o @property

class Caneta1:
    def __init__(self, cor1):
        self.cor_tinta2 = cor1

    @property
    def get_cor2(self):
       return self.cor_tinta2


caneta = Caneta1("Branco")
print(caneta.get_cor2) # nesse caso usando o property você não precisa passar executando a função
# e também você não precisa mudar o nome de toda variavel
# Apenas do atributo da classe