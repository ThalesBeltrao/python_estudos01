# Treinar a interação do for com o dicionario

pessoa = {"nome": "Thales", "idade": 33, "cidade": "São Paulo"}

#print(pessoa)

# apenas as chaves
#for chave in pessoa:
    #print(chave, pessoa[chave])

#print()

# passando pelos os valores
#for c , v in pessoa.items():
    #print(f"{c}: {v}")

#print()

# somar todos os valores das cheves
numero = {"a": 10, "b": 20, "c": 30}
soma = 0

for v in numero.values():
    soma +=v
#print(soma)
#print()




# Conte quantos valore são maiores que 50
notas = {"joao": 70, "maria": 45, "luiz": 90}
contador = 0

for v in notas.values():
    if v > 50:
        contador +=1 # aqui conta quantas vez o contador conta conforme a condição

#print(contador)
#print()
# Criar um novo dicionario so com valores acima de 100

produtos = {"p1": 50, "p2": 120, "p3": 500, "p4": 90}
caro = {}


for k, v in produtos.items():
    if v > 100:
        caro[k] = v

#print(caro)

produtos.setdefault("p5", 1000)
#print(produtos)

# Apaga o ultimo valor
produtos.popitem()
print(produtos)

# Apaga a chave e o valor específicado
produtos.pop("p1")
print(produtos)