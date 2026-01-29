# Pode usar programação funcional com o Filter
# ou fazer listcompreenshion


produtos = [
    {"nome": "produto", "preco": 10.00},
    {"nome": "produto", "preco": 22.32},
    {"nome": "produto", "preco": 7.5},
    {"nome": "produto", "preco": 105.69},
    {"nome": "produto", "preco": 35.99},

]


filtro_produto = [p for p in produtos if p["preco"] > 100.00]

# Uma maneira de realizar a quebra e descompactar a lista ou fazer um for
#print(*filtro_produto, sep="\n")

# Usando o for
for i in filtro_produto:
    print(i)

print()
# Usando agora a programação funcional filter


resultado_filter = filter(lambda p: p["preco"] > 10, produtos)
print(*list(resultado_filter), sep="\n")