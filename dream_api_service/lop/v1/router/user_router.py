# type: ignore
from fastapi.params import Depends

from interface.generic_router import GenericRouter
from middlewares import db_session_middleware
from models.portfolio import PortfolioPydantic

from models.user import UserPydantic, User

from lop.v1.service.user_service import UserService


class UserRouter(GenericRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_service = UserService()
        self.bind_routes()

    def bind_routes(self):
        self.get_router().get("/{username}")(self.get_user_by_username)
        self.get_router().get("/{username}/{password}")(self.check)
        self.get_router().get("/month/{user_id}/{month}")(self.get_calendar_month)   
        self.get_router().get("/day/{user_id}/{date}")(self.get_calendar_day)   
        self.get_router().post("/")(self.create_user)
        self.get_router().post("/create/portfolio")(self.create_portfolio)
        self.get_router().get("/admin/")(self.admin)
        self.get_router().post("/update/{username}/{new_name}")(self.update_username)
        self.get_router().get("/stat/")(self.user_status)
        self.get_router().get("/last/")(self.last_active)

    def last_active(
        self,
        session : db_session_middleware = Depends()
    ):
        return self.user_service.last_active(session)

    
    def user_status(
        self,
        session : db_session_middleware = Depends()
    ):
        status = self.user_service.user_status(session)
        return status

    def update_username(
        self,
        username : str,
        new_name : str,
        session : db_session_middleware = Depends()
    ):
        self.user_service.user_update(username, new_name, session)
        return True

    def admin(
        self, 
        session : db_session_middleware = Depends()
    ):
        print("here")
        users = self.user_service.admin(session)
        return users 

    def create_user(
        self, 
        data : UserPydantic = Depends(),
        session : db_session_middleware = Depends()
    ):
        '''Create a new user from the database and  session database settings'''
        user_id = self.user_service.create_user(data, session)
        return user_id
    
    def create_portfolio(
        self,
        user_id : str,
        data :  PortfolioPydantic = Depends(),
        session : db_session_middleware = Depends()
    ):
        '''Create a new portfolio from the database and  session database settings'''
        portfolio = self.user_service.create_portfolio(user_id, data, session)
        return portfolio

    def get_user_by_username (
        self,
        username : str,
        session : db_session_middleware = Depends()
    ):

        '''Get user by username and session database settings'''
        user = self.user_service.get_user_by_username(username, session)
        return user
    
    def check(
        self,
        username : str,
        password : str,
        session : db_session_middleware = Depends()
    ):
        ''' Bu fonksiyon kullanıcı adı ve şifre kontrolü yapar, hata varsa false döndürür.'''
        result = self.user_service.check(username, password, session)
        if result is True:
            self.user_static = username
        return result
    
    def get_calendar_month(
        self,
        service_id : str,
        user_id : str,
        year : int,
        month : int,
        session : db_session_middleware = Depends()
    ):
        ''' Verdiğin service_id ye sahip olan işin rezervasyonunun yapılabileceği günleri sana liste olarak verir'''
        return self.user_service.get_calendar_month(service_id, user_id, year, month, session)
    
    def get_calendar_day(
        self,
        service_id : str,
        user_id : str,
        date : str,
        session : db_session_middleware = Depends()
    ):
        ''' Verdiğin service_id ye sahip olan işin rezervasyonunun yapılabileceği saatleri sana liste olarak verir'''
        return self.user_service.get_calendar_day(user_id, service_id, date, session)