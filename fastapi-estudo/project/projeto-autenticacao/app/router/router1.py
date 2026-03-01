from fastapi import APIRouter
from router.handlers  import user



router = APIRouter()

router.include_router(
    user.user_router,
    prefix="/users",
    tags=["users"]
)