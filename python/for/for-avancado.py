
lista = [["Nome", "Altura", "Peso"],
         ["Thales", 80.0, 68.5],
         ["Amanda", 62.0, 57.3],
         ["Junior", 90.0, 80.0],
         ["Roberta", 55.0, 50.5]

         ]



# Esse estilo é como se fosse uma tabela com coluna e linhas

for valor_linha, linha in enumerate(lista):
    for valor_coluna, valor in enumerate(linha):
        print(valor_linha, valor_coluna, valor)