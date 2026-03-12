from schema.schema1 import UserAuth
from models.user_model import User
from core.secury import get_password



class UserService:
    @staticmethod
    async def create_user(user: UserAuth):
        usuario = User(
            username= user.username,
            email= user.email,
            hashed_password= get_password(user.password)
        )
        await usuario.save()
        return usuario