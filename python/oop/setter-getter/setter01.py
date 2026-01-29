from numpy.ma.core import around


class Pessoa:
    def __init__(self, idade):
        self._idade = idade

    def get_idade(self):
        return self._idade

    def set_idade(self, nova_idade):
        if nova_idade >=0:
            self._idade = nova_idade
            return f"{self._idade} nova idade"

        else:
            print("idade invalidade")



# aqui voce passa o setter como um metodo da classe
# esse metodo ele modifica o valor original do atributo do objeto
# Setter sem o property
P = Pessoa(10)
#print(P.get_idade())
#print(P.set_idade(20))

class Pessoa1:
    def __init__(self, idade):
        self._idade = idade

    @property
    def idade(self):
        return f"{self._idade}" # Getter

    @idade.setter
    def idade(self, nova_idade):
        if nova_idade >0:
            self._idade = nova_idade
            return f"{self._idade} nova idade"

        else:
            print("idade invalida")

# voce modifica agora o valor do objeto
# Não pelo metodo mas sim adicionando um novo valor a variavel do objeto
# nesse caso ele passou condiçao para alterar o valor
# tem que ser > 0 caso o contrario o valor se manteria
#p1 = Pessoa1(15)
#print(p1.idade)
#p1.idade = 25
#print(p1.idade)



class Conta:
    def __init__(self, saldo):
        self._saldo = saldo

    @property
    def saldo_valor(self): # como se o metodo virasse um atributo retornando o valor do atributo
        return self._saldo # Getter

    @saldo_valor.setter
    def saldo_valor(self, valor):
        if valor >= 500:
            taxa = valor  * 0.8
            self._saldo = taxa
            return self._saldo

        else:
            self._saldo = valor



c1 = Conta(100)
print(c1.saldo_valor)
c1.saldo_valor  = 400
print(c1.saldo_valor)
