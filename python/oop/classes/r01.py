class Pessoa:
    especie = "Humano"
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def especie1(cls, nova_especie):
         cls.especie = nova_especie # Se eu passo com o mesmo nome a variavel ela modifica

p1 = Pessoa("Thales", 33)
Pessoa.especie1("Ciborg")
print(p1.especie)

###############################################











# Criar instâncias alternativas (factory Method)
class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    @classmethod
    def string_data(cls, data_str):
        dia, mes, ano = map(int, data_str.split("/"))
        return cls(dia, mes, ano)


data = Data.string_data("17/11/1991")
print(data.dia)