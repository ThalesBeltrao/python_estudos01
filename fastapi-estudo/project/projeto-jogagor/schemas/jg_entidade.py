def jogadorEntidade(item) -> dict:
    return {
        "id": str(item["_id"]),
        "jg_nome": item["jg_nome"],
        "jg_idade": item["jg_idade"],
        "jg_time": item["jg_time"]
    }

def listaJogadoresEntidade(entity) -> list:
    return [jogadorEntidade(item) for item in entity]

