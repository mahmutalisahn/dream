from middlewares import db_session_middleware
from models.calendar import CalendarPydantic, CalendarSaverPydantic
from ..repositories.calendar_repository import  CalendarRepository

class CalendarService:
    def __init__(self) -> None:
        self.calendar_repository = CalendarRepository()
    
    def create_calendar(
        self, 
        data : CalendarSaverPydantic,
        session : db_session_middleware
    ):
        result = self.calendar_repository.create_calendar(data, session)
        return result
    
    def get_calendar(
        self,
        user_name : str,
        service_id : str,
        session : db_session_middleware
    ):
        result = self.calendar_repository.get_calendar(user_name, service_id, session)
        return result