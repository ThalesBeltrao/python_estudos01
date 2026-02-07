# Melhores Práticas do Fastapi com tratamento de Erro 
# Traatamento de Exceções HTTPException retorno de status code 
# Validação de ID verificação se a string recebida é um ObjectId valido 


from fastapi import APIRouter, HTTPException, status
from config.database import col
from schemas.jg_entidade import jogadorEntidade, listaJogadoresEntidade
from models.jogador import Jogador
from bson import ObjectId
from bson.errors import InvalidId



jg_router = APIRouter(prefix="jogadores", tags=["Jogadores"])


# Validação de  Id 
# O MongoDb exige que o Id seja um tipo de Objeto especial (ObjectId)
# Se você passar uma string normal ele vai dar erro
# Se o usuário digitar um ID que não tem 24 caracteres hexadecimais, o cógido cai no execept
def validar_ip(id_jg: str) -> ObjectId:
    try:
        return ObjectId(id_jg)
    except InvalidId:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="O ID fornecido possui um formato inválido"

        )
 # ---- Rotas (endpoints) ---

########## GET #############
# Listar Jogadores 
@jg_router.get("/jogadores", status_code=status.HTTP_200_OK)
async def listar_jg():
    # Busca todos e converte usando o schema
    jogadores = col.find()
    return listaJogadoresEntidade(jogadores)


# Detalhe de um Jogador 
@jg_router.get("/jogadores/{id_jg}", status_code=status.HTTP_200_OK )
def buscar_jg_id(id_obj: ObjectId= Depends(validar_ip)):
    item_do_banco = col.find_one({"_id": ObjectId(id_obj)})

    if not item_do_banco:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail="Id incorreto ou usuario inexistente"
        )
    return jogadorEntidade(item_do_banco)


########### POST ###############

# Inserir Jogadores
@jg_router.post("/", status_code=status.HTTP_201_CREATED)
def inserir_jg(jogador: Jogador): # recebe o Basemodel
    # Insere no banco
    novo_jg = col.insert_one(dict(jogador))
    # Busca o registro recém criado para confirmar a inserção
    buscado = col.find_one({"_id": novo_jg.inserted_id})
    return jogadorEntidade(buscado)



############ Put ###############

#  Atualiza Jogador 
############ Put ###############

# Atualiza Jogador 
@jg_router.put("/{id_jg}", status_code=status.HTTP_200_OK) # Adicionada a barra inicial
def atualizar(jogador: Jogador, id_obj: ObjectId= Depends(validar_ip)): # Recebe o ID e os novos DADOS
    # 1. Tenta atualizar no banco
        documento_atualizado = col.find_one_and_update(
        {"_id": ObjectId(id_obj)},
        {"$set": dict(jogador)}, # Aqui usamos os dados que vieram do Pydantic
         return_document=True # Força o MongoDB a retornar o documento já alterado
        )
        if not documento_atualizado:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Não foi Possível Atualizar os Dados"
            )
    

@jg_router.delete("/{id_jg}", status_code=status.HTTP_204_NO_CONTENT)
def deletar(id_obj: ObjectId=Depends(validar_ip)):
    deletar = col.find_one_and_delete(
        {"_id": id_obj}
    )
    if not deletar:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
            detail="Jogador Inexistente"
        )
    return None


