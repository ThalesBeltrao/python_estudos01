from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/") # cria a rota que busca a informação
def usuario():
    return {"mensagem": "API rodando"}
