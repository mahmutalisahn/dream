from fastapi.params import Depends

from interface.generic_router import GenericRouter
from middlewares import db_session_middleware

from models.user import UserPydantic, User

from lop.v1.service.user_service import UserService


class UserRouter(GenericRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_service = UserService()
        self.bind_routes()

    def bind_routes(self):
        self.get_router().get("/{user_id}")(self.get_user_by_username)
        self.get_router().get("/{user_name}/{password}")(self.check)        
        self.get_router().post("/")(self.create_user)



    def create_user(
        self, 
        data : UserPydantic = Depends(),
        session : db_session_middleware = Depends()
    ):
        user_id = self.user_service.create_user(data, session)
        return user_id

    def get_user_by_username (
        self,
        username : str,
        session : db_session_middleware = Depends()
    ):
        user = self.user_service.get_user_by_id(username, session)
        return user
    
    def check(
        self,
        username : str,
        password : str,
        session : db_session_middleware = Depends()
    ):
        result = self.user_service.check(username, password, session)
        return result

    