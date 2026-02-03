from pymongo import MongoClient

# Cria um bando de dados 
url = "mongodb://admin:th%40les789@localhost:27017/?authSource=admin"
client = MongoClient(url)

database = client["crud"] # cria um database 
colecao = database["users"] # cria um collection

# insertOne 
#insertOne1 =  colecao.insert_one({"nome": "thales", "email": "thales@gmail.com", "tel": "1299478965"})

# InserMany
#insertMany1 = colecao.insert_many([{"nome":"julia", "email": "julia@hmail.com", "tel": "12987456335"},
                                   #{"nome": "anderson", "email": "anderson@yahoo.com", "tel": "219835558"
                                                                                               #        }])

# bucas todos os dados
find_dados = list(colecao.find())

# Buscar dados especificos 
find_dados_especifico = list(colecao.find({"nome": "thales"}))

# Buscar o primeiro dado usando findOne

primeiro_dados = colecao.find_one({"nome": "julia"})

print(find_dados)
print()

# buscar o primeiro ObjectId

#print(find_dados_especifico)
print()

#print(primeiro_dados)

# filtro especifico

class Cadastro:
    def __init__(self, nome, email, tel):
        self.nome = nome
        self.email = email
        self.tel = tel


    def inserir_dados(self):
        colecao.insert_one({"nome": self.nome, "email": self.email, "tel": self.tel})
        print("dados inseridos")
    



dados = Cadastro("fernando", "fernando@hotmail.com", "655444777")
#dados.inserir_dados()
