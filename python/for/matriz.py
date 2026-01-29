matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for l in matriz:
    #print(l) # retorna todas as linhas que são listas
       pass      # quando você passa por exemplo um indice i[0] retorna o elemento de indice 0 de cada linha
#print()

for linha in matriz:
    for valor in linha:
        pass # dessa forma voce pega os valores de cada linha
        #print(valor, end="")

# aqui voce nao consegue acessar o indice ainda pois não esta usando range(len(matriz) ou enumerate

for i, linha in enumerate(matriz):
    for c, valor in enumerate(linha):
        print(linha[c])