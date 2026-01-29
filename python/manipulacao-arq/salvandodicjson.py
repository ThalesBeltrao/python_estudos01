import json
"""
pessoa = {
    "nome": "thales",
    "sobrenome": "beltrão", # nesse caso por ter caracteres coringa no json fica diferente
    "endereco": [
        {"rua": "R1", "numero": 32},
        {"rua": "R2", "numero": 55}
],
    "altura": 1.8,
    "celular": 12991487091,
}

with open("salvandodicjson.json", "w") as arquivo2:
    json.dump(pessoa, arquivo2, ensure_ascii=False, indent=2) # cria um arquivo em json"""


with open("salvandodicjson.json", "r", encoding="utf8") as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa, sep="\n")
