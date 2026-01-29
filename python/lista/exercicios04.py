#from dados_packege import modulop
from copy import deepcopy

#from dados_packege.modulop import produtos2

novos_produtos = deepcopy(produtos2)


novos_produtos = [{**p, "valor": round(p["valor"] * 1.10)}if p["valor"] >= 10 else{**p}for p in novos_produtos
                  ]

produtos_ordem = sorted(
    novos_produtos,
    key=lambda p: p["valor"])

print(*produtos_ordem,sep="\n")
print()
print(*produtos2,sep="\n")
