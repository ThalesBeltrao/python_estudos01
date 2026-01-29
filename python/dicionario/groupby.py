from itertools import groupby

alunos = [
    {"nome": "Luiz", "nota": "A"},
    {"nome": "Thales", "nota": "A"},
    {"nome": "Letícia", "nota": "B"},
    {"nome": "Roberto", "nota": "C"},
    {"nome": "Amanda", "nota": "D"},
    {"nome": "Julio", "nota": "B"},
    {"nome": "Alice", "nota": "C"},
    {"nome": "João", "nota": "D"},
    {"nome": "Eduardo", "nota": "A"},

    ]


def ordena(aluno):
    return aluno["nota"]


alunos_agrupados = sorted(alunos, key=lambda a: a["nota"])

for aluno2 in alunos_agrupados:
    print(aluno2)
print()


# outra maneira de fazer usando o groupby
grupos = groupby(alunos_agrupados, key=ordena)

for chave, valor in grupos:
    print(chave)
    for aluno in valor:
        print(aluno)
