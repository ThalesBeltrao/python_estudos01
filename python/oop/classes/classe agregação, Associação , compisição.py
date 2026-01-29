
# Relações entre classes: associação, agregação e composição
# Associação é um tipo de relação onde os objetos
# estão ligados dentro do sistema.
# Essa é a relação mais comum entre objetos e tem subconjuntos
# como agregação e composição (que veremos depois).
# Geralmente, temos uma associação quando um objeto tem
# um atributo que referencia outro objeto.
# A associação não especifica como um objeto controla
# o ciclo de vida de outro objeto.


"""class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None


    @property # faz um link
    def ferramenta(self):
        return self._ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta


class FerrametadeEscrever:
    def __init__(self,nome):
        self.nome = nome # nome da ferramenta

    def escrever(self):
        return f"{self.nome} esta escrevendo"


escritor = Escritor("Thales")
caneta = FerrametadeEscrever("Caneta Bick")
maquina_de_escrever = FerrametadeEscrever("Maquina de escrever")
escritor.ferramenta = caneta
escritor.ferramenta2 = maquina_de_escrever

#print(caneta.escrever())

#print(escritor.ferramenta.escrever())
#print(escritor.nome, escritor.ferramenta2.escrever())

#Relação entre Classes: associação, agregação e relação
#Agregação é uma forma mais especializada de associação
#entre dois ou mais objetod. cada objeto tera seu ciclo de vida independente
#geralmente é uma relação de um objeto para muitos objetos
#podem viver separados ou ter dependencias
#outro para fazer determinada tarefa """


class Carrinho:
    def __init__(self):

        self._produtos = []

    #def total(self):
        #return sum([p.preco for p in self._produtos])

    def inserir(self, *args):
        # primeira maneira
        # for produto in produtos:
            # self._produtos.append(produto)
        # segunda maneira
        # self._produtos += produtos

        # terceira opção
        self._produtos.extend(args)

    def listar_produto(self):
        for i in self._produtos:
            print(i.nome, i.preco)


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


carrinho = Carrinho()
p1, p2 = Produto("caneta", 120), Produto("camiseta",20)
carrinho.inserir(p1, p2)
carrinho.listar_produto()




#composição é uma especialidade da agregação
#quando o objeto pai for apagado
#as refencias dos objetos filhos tambem são


"""class Cliente:
    def __init__(self,  nome):
        self.nome = nome
        self.enderecos = []

    def insert_street(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def listar(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)
        return self.listar


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero


cliente = Cliente("Thales")
cliente.insert_street("Avenida lolo", 1000)
cliente.listar()



# AGREGAÇÃO
# Agregação é uma forma mais especializada da associação
# entre dois ou mais objeto"""



