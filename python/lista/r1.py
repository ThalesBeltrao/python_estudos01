
produtos = [{"Nome":"feijão", "preco": 15.20},{"Nome": "Arroz", "preco": 20.00}, {"Nome": "Macarrão", "preco": 3.50}]
alterar = [{**p, "preco": p["preco"] * 2} if p["preco"] > 4 else{**p} for p in produtos]
print(alterar)

####### Trazer apenas os valores alterados

alterar = [{**p, "preco": p["preco"] * 2} for p in produtos if p["preco"] > 4]
print(alterar)

# utilizando map

def alterar_valor(p):
    return [{**p, "preco": p["preco"]* 2} if p["preco"] > 4 else{**p}]


usando_map = list(map(alterar_valor, produtos))
print(usando_map)