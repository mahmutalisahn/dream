# type: ignore
from dream_api_service.middlewares import db_session_middleware
from dream_api_service.models.portfolio import PortfolioPydantic
from dream_api_service.models.user import UserPydantic
from dream_api_service.lop.v1.repositories.user_repository import UserRepository


class UserService :

    def __init__(self) -> None:
        self.user_repository = UserRepository()

    def create_user(
        self, 
        data : UserPydantic,
        session : db_session_middleware
    ):
        user_id = self.user_repository.create_user(data, session)
        return user_id

    def get_user_by_username(
        self, 
        username : UserPydantic,
        session : db_session_middleware
    ):
        user = self.user_repository.get_user_by_username(username, session)
        return user
    
    def create_portfolio(
        self, 
        user_id : str,
        data : PortfolioPydantic,
        session : db_session_middleware
    ):
        portfolio = self.user_repository.create_portfolio(user_id, data, session)
        return portfolio
        
    def check(
        self, 
        username : str,
        password : str,
        session : db_session_middleware
    ):
        result = self.user_repository.check(username, password, session)
        return result

    def get_calendar_month(
        self, 
        service_id : str,
        user_id : str,
        year : int,
        month : int,
        session : db_session_middleware
    ):
        return self.user_repository.get_calendar_month(service_id, user_id, year, month, session)

    def get_calendar_day(
        self, 
        user_id : str,
        service_id : str,
        date : str,
        session : db_session_middleware
    ):
        return self.user_repository.get_calendar_day(service_id, user_id, date, session)