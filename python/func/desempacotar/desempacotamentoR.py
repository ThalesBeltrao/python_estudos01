a, b = 1, 2
a, b = b, a
print(a, b)


pessoa = {
    "nome": "Aline",
    "sobrenome": "Souza",
}

# args e kwars
# args empacotar e desempacotar tuplas e listas
# kwargs desempacotamento e empacotamento de dicionários
# keyword arguments( argumentos nomeados)

c, d = pessoa
# c recebe a usuario nome

# d recebe a usuario sobrenome

print(c)
print(d)


# voce pode pegar os values ou os itens
# ou então pode pegar o valor direto passando entre parenteses

e, f = pessoa.values() # vai pegar apenas os nomes
# print()
g, h = pessoa.items()  # aqui ja passa a usuario e o valor

#print(e, f) # apenas os valores
#print(g, h) # os key e valores

# tem como pegar usuario e valor colando as variáveis entre parenteses

(m1, m2), (n1, n2) = pessoa.items()
# print()
# print(n1, n2)

# empacotamento e desempacotamento em dicionário
# for usuario, valor in pessoa.items():
    # print(usuario, valor)

dados_pessoa = {
    "idade": 16,
    "altura": 1.6
}
# usando uma funcao do dicionário
# pessoa.update(**dados_pessoa) # voce esta desempacotando o diocionario porque ** para referenciar usuario e valor

# criando uma variável

pessoa_completa = {**pessoa, **dados_pessoa} # posso continuar adicionando elementos ao dicionário
print(pessoa_completa)


# posso fazer o desempacotamento usando o for


def mostro_argumentos_nomeados(*args,**kwargs):
    print("Não Nomeados", *args)
    for values, items in kwargs.items():
        print(values, items)


mostro_argumentos_nomeados(nome="Thales", altura=1.8)
print()
mostro_argumentos_nomeados(pessoa_completa)









