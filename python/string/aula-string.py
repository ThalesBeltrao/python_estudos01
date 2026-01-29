# Fatiamento

n = "thales"
#print(n[0])  Primeiro caracter
#print(n[-1]) Ultimo caracter
#print(n[2:4])  Do índice 2 até o 4
#print(n[:4])  Do índice 0 ate o 4
#print(n[::2])  vai pular de 2 em 2
#print(n[::-1])  Invertida

b = " ola, mundo "
print(b.capitalize()) # Deixa a primeira letra em Maiúsculo
print(b.replace("ola", "Hi")) # Altera um valor por outro
print(b.strip()) # tira os espaços sobrando
print()

# Métodos de Busca
print(b.find("o")) # Mostra o Indice nesse caso é 1 porque tem espaço
print(b.startswith(" ")) # Começa com True|False
print(b.endswith("o")) # Termina com
print(b.count("o")) # Contar palavra
print(len(b)) # 12 porque começa do 1



# METODO DE QUEBRE E UNIÃO
g = "Banana, Maça, Pera"
lista = g.split(",") # faz uma lista com a quebra que voce determina
print(lista)
print("-".join(lista))