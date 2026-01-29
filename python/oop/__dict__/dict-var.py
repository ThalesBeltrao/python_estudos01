class Pessoa:
    ano_atual = 2022  # esse atributo é um padrão para toda instancia que é definida

    def __init__(self, nome , idade ):
        self.nome = nome
        self.idade = idade

    def get_anor_nascimento(self):
        return Pessoa.ano_atual - self.idade

# Voce consegue ler e criar os atributos e metodos dentro de um obejto com dict
# Criar, apagar
n1 = Pessoa("thales", 33)
n1.__dict__["Altura"] = 1.8 # que louco né
print(n1.__dict__)

# Vars é uma função mais segura porem executa a mesma ação
print(vars(n1))


# Eu posso desempacotar um dicionário dentro de uma classe atribuindo os devidos
#valores a ela desde que com o mesmo nome de cada tribuito muito gênial

dados = {"nome": "julio", "idade":20}

n2 = Pessoa(**dados) # a classe distribui os valores em cada usuario e valor
n3 = vars(n2)
print(n3)