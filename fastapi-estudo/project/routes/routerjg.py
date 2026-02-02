from fastapi import APIRouter
from config.database import col
from models.jogador import Jogador
from schemas.jg_entidade import jogadorEntidade, listaJogadoresEntidade

jg_router = APIRouter()

@jg_router.get("/jogadores")
async def listar_jg():
    # Busca todos e converte usando o schema
    jogadores = col.find()
    return listaJogadoresEntidade(jogadores)

@jg_router.post("/jogadores")
async def inserir_jg(jogador: Jogador): # recebe o Basemodel
    # Insere no banco
    novo_jg = col.insert_one(dict(jogador))
    # Busca o registro recém criado para confirmar a inserção
    buscado = col.find_one({"_id": novo_jg.inserted_id})
    return jogadorEntidade(buscado)