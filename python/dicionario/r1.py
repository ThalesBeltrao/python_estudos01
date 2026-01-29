# Coonvertendo tupla aninhada em dicionario


dados = (("nome", "thales"), ("idade", 30))
modi_dict = dict(dados)
#print(modi_dict)

# Conversão de Tupla Plana
dados1 = ("nome", "thales", "idade", 30)
modi_dict1 =dict(zip(dados1[::2],dados1[1::2]))
#print(modi_dict1)

# Conversão de lista que contem tuplas para dicionario
dados2 = [("nome", "thales"), ("idade", 30)]
modi_dict2 = zip(dados2[::2],dados2[1::2])
#print(dict(*modi_dict2))

#################################################

pessoa = {
        'nome': "thales".capitalize(),
        "sobrenome": "willian".capitalize(),
        "idade": 15,
        "Altura": 1.80,
        "Endereco":[
            {"rua":"joaquim de oliveira silva", "Numero":1000}
        ]
}
# Buscar pelo valor
print(pessoa["nome"])
print()
# Passar um for para analisar dos dados dentro da variável
for i in pessoa: # outro modo é pessoa.item() que busca tanto a chava como os valores
    pass
    #print(i, pessoa[i])

nome = "Allan"
pessoa["nome"] = nome
print(pessoa)

# Criar um Dicionário Dinamico
# Quantas chaves
usuario = "nome_paciente"
idade_usuario = "idade_isuario"
dados_paciente = {usuario: "Thales Willian", idade_usuario: 33}
dados_paciente[idade_usuario] = 44
print(dados_paciente.values())


def convercao_dic(dados):
    modi_dict7 = dict(dados)
    return modi_dict7


valor = convercao_dic(dados)
print(valor)

