from fastapi import APIRouter, HTTPException, status
from schema.schema1  import UserAuth, UserDetail
from services.service01 import UserService
import pymongo
from pymongo import errors


user_router = APIRouter()

@user_router.post("/add", summary="adicionar usuario", response_model=UserDetail)
async def add_usuario(data: UserAuth):
    try:
        return await UserService.create_user(data)
    except errors.DuplicateKeyError:
        raise HTTPException (
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="username ou email ja existe"
        )