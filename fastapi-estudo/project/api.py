from fastapi import FastAPI
import uvicorn
from routes.router_jg import jg_router

app = FastAPI()

app.include_router(jg_router)