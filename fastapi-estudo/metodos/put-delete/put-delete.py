from  fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Base para a criação do post 
class Pessoa(BaseModel):
    nome: str
    altura: float
    peso: float

# Base para a criaçao do Put
class Atualizar(BaseModel):
    nome: Optional[str] = None
    altura: Optional[float] = None
    peso: Optional[float]  = None


dados = {}
id_pessoa = 1

# funcao chegar dados

def checagem_dado(dados_novos):
   for i in dados.values(): # values = key, values
       if i == dados_novos:
           return True
   return False


@app.post("/pessoa")
def criar_pessoa(pessoa: Pessoa):
    global id_pessoa
    novo = pessoa.dict()

    if checagem_dado(novo):
        return {"Pessoa": "Existentes"}

    dados[id_pessoa] = novo
    id_pessoa += 1
    return {"Pessoa": "Criado com sucesso"}


@app.get("/pessoa/{id}")
def buscar_pessoa(id: int):
   if id in dados:
       return dados[id]

   raise HTTPException(404, detail="id nao existente")


@app.put("/pessoa/{id}")
def atualizar(id: int, pessoa: Pessoa):
    if id not in dados:
        return {"Pessoa": "Nao encontrada"}
    
    dados_atuais = dados[id]

    if pessoa.nome is not None:
        dados_atuais["nome"] = pessoa.nome
    if pessoa.altura is not None:
        dados_atuais["altura"] = pessoa.altura
    if pessoa.peso is not None:
        dados_atuais["peso"] = pessoa.peso
    
    dados[id] = dados_atuais
    return{"Pessoa": "Atualizada com sucesso"}



@app.delete("pessoa/{id}")
def delete(id: int):
    if id in dados:
        del dados[id]
        return {"Pessoa": "Deletada com sucesso"}