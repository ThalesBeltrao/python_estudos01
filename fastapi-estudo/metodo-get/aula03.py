import uvicorn
from fastapi import FastAPI, HTTPException

#trabalhando com parametros e querys
# parametros na rota voce passa o id
#  buscar por id
# buscar por elementos com código

# requisação modelo query strig ?

# Para que servem
# filtros
# Paginação
# Ordenação
# Parametros opcionais

# ge-jogador/1?id=1



app = FastAPI()

dados = {
    1: {"nome": "Thales",
        "idade": 34,
        "altura": 1.8,
        "posicao": ["atacante", "meio-armador"],
        "time": "Santos"
    },
    2: {"nome": "Jonas",
        "idade": 25,
        "altura": 1.7,
        "posicao": ["lateral"],
        "time": "Vasco"
    }
}

@app.get("/jogadores/time")
def dados_jogador(time: str):
    for jogador_id in dados:
        if dados[jogador_id]["time"] == time:
            return dados[jogador_id]

        raise HTTPException(status_code=404, detail="time não encontrado")

for id in dados:
    print(dados[id])