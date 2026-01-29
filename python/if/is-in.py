# Is serve para fazer uma comparação
# Para analisar se a mesma variável aponta para o mesmo local
# Muito utilizado em None

x = None
print(x is None) # retorna um elemento True ou False

l1 = [1,2,3,4,5]
l2 = [1,2,3,4,5]
l3 = l1 # Lembrando que valores mutáveis como lista voce não copia ela, apenas aponta para o mesmo local
# quando cria uma variável e faz ela receber a outra variáveis com os valores mutáveis

print(l1 is l2) # Por mais que a lista tenha o mesmo tamanho e os mesmo elementos
# elas são diferentes porque estão alocadas em lugares distintos
print(l1 is l3)
print()
print("Resultado do IN")


# In serve para verificar se um elemento esta na dentro de um acadeia de elementos
# como uma lista, tuplas, a própria string


print(2 in l1) # quer dizer que o elemento esta dentro daquela cadeia de elemento

# Em dicionários apenas faz a verificação das Keys usando o *in*

item10 = {"Nome": "Thales", "Altura": 1.8}
print("Nome" in item10)

