import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

# Criar o Objeto app
app = FastAPI()

# Criar a Classe contando o BaseModel
# Base model é para receber os dados do front
class Jogador(BaseModel):
    nome: str
    idade: int
    altura: float
    posicao: list[str]

# Para atualizar precisa criar um novo BaseModel
class atualizar(BaseModel):
    nome: Optional[str] = None # regra de nogocio que é opicional
    idade: Optional[int] = None
    altura: Optional[float] = None
    posicao: Optional[list[str]] = None



# Criar um dicionario e um contador
# O contador vai servir para gerar os id do dicionário

dados_jg = {} # como se fosse um banco de dados
id_jg = 1

# agora precisarmos criar um função
# que faz a checagem se tem id com os mesmos valores
def checar_dados(novo_dados): # aqui onde os dados novos vão passar para checagem
    for j in dados_jg.values(): # checagem chave e valor
        if j == novo_dados:
            return True
    return False


@app.post("/jogadores")
def insert_via_post(jg: Jogador):
    global  id_jg # torna os dados da varivável acessível para fora do escopo

    novo = jg.dict() # cria a variável para transformar os dados em Dict

    if checar_dados(novo): # apenas passa o if porque a propria função ja faz a checagem
        return {"Dados": " Ja exixtem"} # quebra o código aqui

    dados_jg[id_jg] = novo # o numero do id recebe a nova variável
    id_jg += 1
    return {"Jodador criado com sucesso", id_jg}


@app.get("/jogadores/{id}")
def buscar_dados(id: int):
    if id in dados_jg:
        return dados_jg[id]

    elif id not in dados_jg:
        return {"Dados": "Inexistente"}


@app.put("/atualizar_jogador/{id}")
def atualizar_dados(id:int, jogador: atualizar):
    if id not in dados_jg:
        return {"Erro": "Jogador não existe"}

    jogador_atual = dados_jg[id]
    # Aqui ele pegada todo o dicionario para ele

    if jogador.nome is not None:
        jogador_atual["nome"] = jogador.nome

    if jogador.idade is not None:
        jogador_atual["idade"] = jogador.idade

    if jogador.altura is not None:
        jogador_atual["altura"] = jogador.altura

    if jogador.posicao is not None:
        jogador_atual["posicao"] = jogador.posicao

    dados_jg[id] = jogador_atual

    return {
        "mensagem": "Jogador atualizado com sucesso",
        "dados": jogador_atual
    }



@app.delete("/jogador_excluir/{id}")
def excluir_dados(id: int):
    if id in dados_jg:
        del dados_jg[id]
        return { f"Excluido": "Jogador excluido com sucesso"}, dados_jg
    return {'Erro': "Jogador Inexixtente"}
