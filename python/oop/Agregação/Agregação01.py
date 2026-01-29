class Quarto:
    def __init__(self, numero):
        self.numero = numero

    def __str__(self):
        return f"Quarto {self.numero}"


class Sala:
    def __init__(self, tamanho):
        self.tamanho = tamanho

    def __str__(self):
        return f"Sala de tamanho {self.tamanho}"


class Casa:
    def __init__(self, quarto, sala):
        self.quarto = quarto
        self.sala = sala

    def descricao(self):
        return f"A casa tem um {self.quarto} e uma {self.sala}."

# Criando instâncias das classes


quarto_principal = Quarto(1)
sala_estar = Sala("grande")

# Agregando os objetos criados na classe Casa
minha_casa = Casa(quarto_principal, sala_estar)
print(minha_casa.descricao())