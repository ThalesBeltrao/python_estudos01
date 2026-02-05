from fastapi import APIRouter
from config.database import col
from schemas.jg_entidade import jogadorEntidade, listaJogadoresEntidade
from models.jogador import Jogador
from bson import ObjectId



jg_router = APIRouter()

########## GET #############
# Listar Jogadores 
@jg_router.get("/jogadores")
async def listar_jg():
    # Busca todos e converte usando o schema
    jogadores = col.find()
    return listaJogadoresEntidade(jogadores)


# Detalhe de um Jogador 
@jg_router.get("/jogadores/{id_jg}")
def buscar_jg_id(id_jg):
    item_do_banco = col.find_one({"_id": ObjectId(id_jg)})
    return jogadorEntidade(item_do_banco)







########### POST ###############

# Inserir Jogadores
@jg_router.post("/jogadores")
async def inserir_jg(jogador: Jogador): # recebe o Basemodel
    # Insere no banco
    novo_jg = col.insert_one(dict(jogador))
    # Busca o registro recém criado para confirmar a inserção
    buscado = col.find_one({"_id": novo_jg.inserted_id})
    return jogadorEntidade(buscado)



############ Put ###############

#  Atualiza Jogador 
############ Put ###############

# Atualiza Jogador 
@jg_router.put("/jogadores/{id_jg}") # Adicionada a barra inicial
def atualizar(id_jg: str, jogador: Jogador): # Recebe o ID e os novos DADOS
    # 1. Tenta atualizar no banco
    col.find_one_and_update(
        {"_id": ObjectId(id_jg)},
        {"$set": dict(jogador)} # Aqui usamos os dados que vieram do Pydantic
    )
    
    # 2. Busca o documento atualizado para retornar
    documento_atualizado = col.find_one({"_id": ObjectId(id_jg)})
    
    if not documento_atualizado:
        return {"erro": "Jogador não encontrado"}
        
    return jogadorEntidade(documento_atualizado)