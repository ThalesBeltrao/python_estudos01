"""
Sets
Conjuntos em python
Sests são mutáveis
Aceita apenas valores imutaveis como valores internos
"""


# Sets são eficientes para remover valores duplicados
#de iteraveis
# eles não tem indexes
# eles não garantem ordem
# eles são iteráveis (form in, in not)


#metodos Uteis
# add, update, clear, discard
#Operadores úteis:
#união | união(union) - une
#intersecção & (intersection)- itens presentes em ambos
#diferença _itens presentes apenas no set da esquerda

#s1 = set() # [] lista {} dicionario () tuple set tem que declarar
#s1 = {"nome",1,2,3} # set com dados
#print(type(s1))

#s1 = {1,2,3,3,3,3}# eliminam valores duplicados
#print(s1)

#s2 = [1,1,1,2,3,3,3]
#print(s2)
#s3 = set(s2)
#print(s3) # nesse caso converte a lista com valores repetidos para set que deixa apenas os valores que não são repetidos depis converte para lista novamente
#s4 = list(s3)
#print(s4)


"""s1 = set()
s1.add("luiz")
s1.add(1)
s1.update(("ola mundo",1,2,3)) # nesse caso é preciso colocar parenteses dentro de parenteses
#s1.clear() faz a limpesa
s1.discard("ola mundo") # descarta o valor que voce passou nelo 
print(s1)"""

#união |
#intersecção &
# diferença -
#diferença simétrica ^ ITENS QUE NÃO ESTÃO EM AMBOS
s1 = {1, 2, 3}
s2 = {2, 3, 4}
#s3 = s1.difference(s2)# aqui busca apenas os valores diferentes entre s1 e s2
#s4 = s2.difference(s1)
#s5 = s1.intersection(s2) # valores iguais entre os conjuntos
#print(s3)
#print(s4)
#print(s5)

s3 = s1 | s2 # nesse caso se faz a união entre os conjuntos
s4 = s1 & s2   # intersecção entre eles valores iguais compartilhados
s5 = s1 - s2# a diferença entre eles
s6 = s2 - s1# a diferença entre eles
s7 = s1 ^ s2 # numeros que  não estão em ambos

print(s3)
print(s4)
print(s5)
print(s6)
print(s7)


letras = set( )
while True:
    adivinhe  = input("Digite: ")
    letras.add(adivinhe.lower())

    if "l" in adivinhe:
        print("Parabens você acertou ")
        break 

