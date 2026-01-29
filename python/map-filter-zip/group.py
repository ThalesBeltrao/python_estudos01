from itertools import groupby

alunos1 = [ {"nome": "luiz", "nota": "A"},
         {"nome": "Thales", "nota": "D"},
         {"nome": "Alice", "nota": "B"},
         {"nome": "Vanessa", "nota": "C"},
         {"nome": "Bruno", "nota": "A"},
         {"nome": "Bruno", "nota": "D"},
         {"nome": "Bruno", "nota": "C"},



        ]


# Essa lista quando você organiza por grupo
# Ele apenas guarda os elementos na sequência
# caso saia da sequência ele cria outro indices
#alunos = ["a","a","a", "b", "c","a"]
# usando o groupby em dicionários funciona de maneira diferente.
#grupos = groupby(alunos1) # usando o sorted ele agrupa os elementos que são iguais
# mesmo que estejam fora de ordem
#print(next(grupos))

# ordenação de dicionários
alunos_agrupados = sorted(alunos1, key=lambda a:a["nota"])

# usando o groupby
grupos = groupby(alunos_agrupados, key=lambda a:a["nota"] )


# Esse for ele vai separar alunos com as mesmas notas
for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)


