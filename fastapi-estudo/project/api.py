from fastapi import FastAPI
import uvicorn
from routes.routerjg import jg_router

app = FastAPI()

app.include_router(jg_router)