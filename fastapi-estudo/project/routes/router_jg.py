from fastapi import APIRouter,HTTPException
from config.database import  listar
from models.jogador import Jogador

jg_router = APIRouter()




@jg_router.get("/jogadores")
async def listar_jg():
    return listar()