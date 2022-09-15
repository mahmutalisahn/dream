
from models.user import UserPydantic, User
from middlewares import db_session_middleware

import uuid

class UserRepository:

    def create_user(
        self,
        data = UserPydantic,
        session = db_session_middleware
    ):
    
        user = User()
        user.email = data.email
        user.username = data.username
        user.name = data.name
        user.surname = data.surname
        user.user_id = str(uuid.uuid1())
        user.password = data.password
        
        if data.phone != None:
            user.phone = data.phone

        session.add(user)
        session.commit()

        return user.username

    def get_user_by_id(
        self,
        user_id : str,
        session : db_session_middleware
    ):
        user = session.query(User).filter(User.user_id == user_id).first()
        return user

    def get_user_by_username(
        self,
        username : str,
        session : db_session_middleware
    ):
        user = session.query(User).filter(User.username == username).first()
        return user

    def check(
        self,
        username : str,
        password : str,
        session : db_session_middleware
    ):
        user = self.get_user_by_username(username, session)
        
        if user is not None:
            if user.password == password:
                return user
        
        return False

