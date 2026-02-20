from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from routes.routerjg import jg_router

# Configuração do CORS
cliente_app = [

    "http://localhost:3000"
]



app = FastAPI()

# Incluir a rota
app.include_router(jg_router)

# quais clientes podem comunicar com a api
app.add_middleware(
    CORSMiddleware,
    allow_origins= cliente_app,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]

)