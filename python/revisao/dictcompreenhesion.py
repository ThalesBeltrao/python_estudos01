produto = {
    "nome:": "Caneta Azul",
    "preco:": 2.5,
    "categoria:": "Escritório"
}


for k, v in produto.items():
    print(k, v)


# fazendo dictcompreenhesion
# voce pode fazer uma condicional com os valores
# se usuario for da instância str então ele aplica o capitalize se não retorna o valor padrão
dc = {
    chave.capitalize(): valor.capitalize()
    if isinstance(valor, str) else valor
    if isinstance(chave, str) else chave
    for chave, valor in produto.items()
}
print()
print(dc, sep="\n")


# voce pode fazer um dicionario  a partir de uma lista que contem uma tupla
# que parece ter usuario a valor

lista = [
    ("A", "valor A"),
    ("B", "valor B"),
    ("C", "valor C"),
]

new_dict = {
    chave: valor
    for chave, valor in lista
}

# posso fazer a conversão nesse caso
# com o objeto dict

print(dict(**new_dict))


# set compreenhesion

