from produto import Produto


class Carrinho:
    def __init__(self):
        self._produtos = []


    def add_produto(self, produto: Produto):
        self._produtos.append(produto)


    def listar_produto(self):
        for p in self._produtos:
           p.info_produto()

    def somar(self):
        return f"Valor Total R$:{sum(p.valor for p in self._produtos)}"







