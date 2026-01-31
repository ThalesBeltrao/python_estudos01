import uvicorn
from fastapi import FastAPI, HTTPException

# Path Parameter
# Identificar Recursos específicos
# Por exemplos id ele vai direto depois do caminho da path
# O que define ser um path parameter é a chave {}

app = FastAPI()

dados = {
        1: {"nome": "thales".capitalize(),
            "idade":34,
            "altura": 1.8,
            "posicao": ["atacante", "meio-armador"]

    },
        2: {"nome": "jonas".capitalize(),
            "idade": 25,
            "altura": 1.7,
            "posicao": ["lateral"]
        }
    }

@app.get("/{id}")
def dados_jogador(id:int):
        if id not in dados:
            raise HTTPException(
                status_code=404,
                detail= "recurso não encontrado"
            )
        return dados[id]

    # caso de erro mostra uma mensagem que não tem o id
    # caso tenha retorna o id buscado pelo get