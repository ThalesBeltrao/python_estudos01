from fastapi import FastAPI
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
import uvicorn
from config.config import settings01
app = FastAPI(
    title=settings01.PROJECT_NAME,
    openapi_url=f"{settings01.API_V1_STR}/openapi.json"
)




@app.on_event("startup")
async def app_init():
    cliente_db = AsyncIOMotorClient(
        settings01.MONGO_CONNECTION_STRING
    ).todoapp

    await init_beanie(
        database= cliente_db,
        document_models=[
        ]
    )