from unittest import result
from models.calendar import Calendar, CalendarPydantic
from middlewares import db_session_middleware

class CalendarRepository:
    
    def create_calendar(
        self, 
        data : CalendarPydantic,
        session : db_session_middleware
    ):
        calendar = Calendar()
        calendar.service_id = data.service_id
        calendar.user_name = data.user_name
        calendar.monday = data.monday
        calendar.tuesday = data.tuesday
        calendar.wednesday = data.wednesday
        calendar.thursday = data.thursday
        calendar.friday = data.friday
        calendar.saturday = data.saturday
        calendar.sunday = data.sunday

        session.add(calendar)
        session.commit()

        return calendar.service_id


    def get_calendar(
        self, 
        user_name : str,
        service_id : str,
        session : db_session_middleware
    ):  
        calendar = session.query(Calendar).filter(Calendar.service_id == service_id and Calendar.user_name == user_name).first()
        return calendar
    
