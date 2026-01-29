class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def info_produto(self, *args):
        print("Produto: {} Valor R$: {}".format(self.nome, self.valor))



