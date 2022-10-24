from unittest import result
from fastapi.params import Depends

from dream_api_service.interface.generic_router import GenericRouter
from dream_api_service.middlewares import db_session_middleware
from dream_api_service.models.calendar import CalendarPydantic, CalendarSaverPydantic

from ..service.calendar_service import CalendarService

class CalendarRouter(GenericRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.calendar_service = CalendarService()
        self.bind_routes()
    
    def bind_routes(self):
        self.get_router().get("/{user_name}/{service_id}")(self.get_calendar)
        self.get_router().post("/")(self.create_calendar)
        
    def create_calendar(
        self, 
        data : CalendarSaverPydantic = Depends(),
        session : db_session_middleware = Depends()
    ):
        '''Create a calendar from the given data. \nData format is " StartTime_EndTime_LaunchTimeStart_LaunchTimeEnd "\nIf user not working, send "Not Working" message.'''
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
