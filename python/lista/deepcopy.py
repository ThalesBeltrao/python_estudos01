"""Cuidado com dados mutáveis
 = - copiando valor(imutáveis)
 = - aponta para o mesmo valor da memória(mutável)"""
import copy

#nome = "luiz"
#nome = "joão"
# print(nome) # você sobreescreveu a variável

#nome1 = "thales"
#salvando_nome = nome1
#nome1 = "jander"
# nesse caso antes de sobreescrever o valor ele salva em outra variável antes
#print(nome1)
#print(salvando_nome)

# valores imuttavis como string ou int, float ele sobreescreve esses valores
# diferente de mutáveis como lusta, tuplas, dicionários

lista = ["Thales", "Amanda"," Roberto"]
lista_b = lista
#print(lista_b) # e se eu alterar a lista b tambem modifica a lista a

# copy
lista_c = copy.deepcopy(lista_b) # apenas para lista com elementos imutaveis ja não fuunciona se estiver dentro desta lista outra lista
lista_c[0] = "José"
print()
print(lista_c)

