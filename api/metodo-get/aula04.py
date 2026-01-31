import uvicorn
from fastapi import FastAPI

app = FastAPI()

DB_PRODUTOS = {
    1: "Mouse Gamer",
    2: "Teclado Mecânico",
    3: "Monitor Ultrawide",
    4: "Cadeira Ergonômica",
    5: "Headset Bluetooth",
    6: "Webcam Full HD",
    7: "Placa de Vídeo RTX 4080",
    8: "Processador Core i9",
    9: "Memória RAM 32GB",
    10: "Gabinete Mid Tower",
}

# A lista ordenada das chaves do dicionário, para aplicar 'ignorar' e 'limite'
IDS_PRODUTOS = list(DB_PRODUTOS.keys())
# IDS_PRODUTOS é [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

@app.get("/item/{id_item}")
def ler_item(id_item: int):
    if id_item in DB_PRODUTOS:
        return {
            "id_item": id_item,
            "produto": DB_PRODUTOS[id_item],
            "uso": "Path Parameter"
        }


