# como se fosse teoria do conjunto
# sets são mutável, mas aceita apenas valores imutável
# eficientes para remover valores duplicados


s1 = set("Thales") # passando a classe ele pode vim fora da ordem
s2 = {"Thales", 10, 10.20} # dessa maneira não
#print(s1)
#print(s2)

s3 = {1, 2, 2, 3, 3, (1, 2, 3, "Junior")} # eles só troca de ordem quando tem elementos diferentes dentro dele
#print(s3)

# remoção de valores duplicados com set

l1 = [1, 1, 1, 2, 2, 3, 3, ]
l2 = set(l1)
l2 = list(l2)
#print(l2)

# posso usar in , not in e for tambem
#print(3 in s3)
#for i in s3:
    #print(i)

# Operadores Uteis
# união(union) une um set com outro
# intersecção & intersection - Itens presentes em ambos
# diferença - Item presentes apenas no set da esquerda
# diferença simétrica ^- itens que não estão em ambos


s4 = set()
s4.add(1)

s4.update("thales")
#print(s4)

# para eu passar um interavel inteiro tem que ser dentro de uma tupla
s4.update(("Junior", 10))
#print(s4)

# discard = descartar um valor passando o proprio valor

# s4.discard("thales")
# s4.discard("Junior")
# s4.discard(10)
#print(s4)

n1 = {1, 2, 3}
n2 = {2, 3, 4}

# uniao |

# n3 = n1 | n2
# print(n3)

# union
    #  n1.union(n2)
    # print(n1)

# diferença

# n3 = n1 - n2
# n4 = n2 - n1
# print(n3)
# print(n4)

# diferença com operador

# (n1.difference(n2))
# print(n2.difference(n1))

# interseção igual em ambos

n3 = n1 & n2

print(n3)

# Projetos
