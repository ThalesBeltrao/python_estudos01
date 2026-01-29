class Carrinho:
    def __init__(self):
        self.produto = []

    def add_produto(self, *produto):
        self.produto.extend(produto)


    def listar_produto(self):
        for i in self.produto:
            return f"{i.nome},R$:{i.valor}"




class Produto:
    def __init__(self,nome, valor):
        self.nome = nome
        self.valor = valor



cerveja = Produto("sckol", 4.00)
carrinho = Carrinho()
carrinho.add_produto(cerveja)
print(carrinho.listar_produto())



