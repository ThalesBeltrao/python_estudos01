from pydantic import BaseModel



class Jogador(BaseModel):
    jg_nome: str 
    jg_idade: int
    jg_time: str 