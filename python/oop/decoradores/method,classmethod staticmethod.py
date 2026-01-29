class Connection:
    def __init__(self, host="localhost"):
        self.host = host
        self.user = None
        self.password = None



    def set_user(self, user):  # nesse caso ele a classe uma essa funcao como um set ele busca a variavel do self e coloca um valor nele
        self.user = user

    def set_password(self, password):
        self.password = password




c1 = Connection()
c1.set_user("thales")

c1.set_password(123)
print(c1.user, c1.password)
print(c1.host)
