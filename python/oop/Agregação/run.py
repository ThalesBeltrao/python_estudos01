from produto import Produto
from carrinho import Carrinho




cerveja = Produto("Estela", 3.50)
refrigerante = Produto("Coca", 7.50)
bola = Produto("Nike", 50.00)
carrinho = Carrinho()
carrinho.add_produto(cerveja)
carrinho.add_produto(refrigerante)
carrinho.add_produto(bola)
carrinho.listar_produto()
print(carrinho.somar())