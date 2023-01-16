# type: ignore
from middlewares import db_session_middleware
from models.portfolio import PortfolioPydantic
from models.user import UserPydantic
from lop.v1.repositories.user_repository import UserRepository
from lop.v1.service.booking_service import BookingService

class UserService :

    def __init__(self) -> None:
        self.user_repository = UserRepository()
        self.booking_service = BookingService()

    def user_status(
        self,
        session : db_session_middleware
    ):
        user_status = self.user_repository.user_status(session)
        service_status = self.booking_service.service_status(session)

        return [{
            "Number of the active user : " : user_status,
            "Number of the bookings : "  : service_status
        }]

    def last_active(
        self,
        session : db_session_middleware
    ):
        user = self.user_repository.last_active(session)
        return user

    def admin(
        self,
        session = db_session_middleware
    ):
        users = self.user_repository.get_user_all(session)
        return users     

    def user_update(
        self,
        username : str,
        new_name : str,
        session : db_session_middleware
    ):
        self.user_repository.update_username(username, new_name, session)
        return True

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
        return_user = UserPydantic()
        
        return_user.ssn = user.ssn
        return_user.name = user.name
        return_user.surname = user.surname
        return_user.email = user.email
        return_user.phone = user.phone

        return return_user
    
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
        
        if result is not None:
            return self.booking_service.get_booking(username, session)
        
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