from unittest import result
from fastapi.params import Depends

from interface.generic_router import GenericRouter
from middlewares import db_session_middleware
from models.calendar import CalendarPydantic

from ..service.calendar_service import CalendarService

class CalendarRouter(GenericRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.calendar_service = CalendarService()
        self.bind_routes()
    
    def bind_routes(self):
        self.get_router().get("/{user_name}/{service_id}")(self.get_calendar)
        self.get_router().post("/")(self.create_service)
        
    def create_service(
        self, 
        data : CalendarPydantic = Depends(),
        session : db_session_middleware = Depends()
    ):
        result = self.calendar_service.create_calendar(data, session)
        return result
    
    def get_calendar(
        self, 
        user_name : str,
        service_id : str,
        session : db_session_middleware = Depends()
    ):
        result = self.calendar_service.get_calendar(user_name, service_id, session)
        return result
