def adiciona_clientes(nome, lista=[]):
    lista.append(nome)
    return lista

lista =[] # agora o problema esta resolvido porque voce para o parametro lista
client1 = adiciona_clientes("luiz", lista)
adiciona_clientes("joana", client1)
print(client1)

cliente2 = adiciona_clientes("thales")
adiciona_clientes("amanda", cliente2)
print(cliente2) # ela não gera outra lista ela adiciona os elementos da lista atinga



# nos casos de ser parametros mutáveis ele usa a mesma lista sempre mesmo com outra variavel
#se voce não definir nada dentro do paramtro mutável e deixar ele vazio
#resolvendo problema cria uma lista vazia e passa dentro da def

#segundo modo é passar um none para a lista ou definir uma condicional dentro dela para ela criar uma lista caso seja none o argumento que não foi passado para o parametro da funcao



def add_clientes(nome, lista=None):
    if lista is None:
        lista2 = []
        lista.append(nome)
        return lista


clientes3 = add_clientes("thales") #   o if não deixa quebrar o codigo porque caso seja None ele cria uma lista jogando o valor que foi passado na variável

print(clientes3)