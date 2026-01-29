#escopo de classe e de métodos de classe
class Animal:
    def __init__(self, nome):
        self.alimento = None
        self.nome = nome

    def comendo(self, alimentos): # self global da classe pode pode passar outros parametros para ela
        self.alimento = alimentos
        #print("{} esta executando uma ação".format(self.nome))
        return "{} esta comendo um {} ".format(self.nome, alimentos) # esta salvando o valor para ser passado para uma variavel ou executado dentro de uma funçao igual o print



leao = Animal("Leão")
alimento = Animal.comendo(leao,"macarrão")
print(leao.nome)
                                  #leao.acao() # nesse caso vai vim um none e o valor que foi passado para a funão acao porque o print e um metodo(ação) dentro da classe
print(leao.comendo("macarrão"))   #self do escopo primario que é o nome do animal ja foi definido na primeira funcao na segunda que é o nome do alimento voce vai passar ela quando chamar a funcao fora do escopo
print(alimento)   #self do escopo primario que é o nome do animal ja foi definido na primeira funcao na segunda que é o nome do alimento voce vai passar ela quando chamar a funcao fora do escopo