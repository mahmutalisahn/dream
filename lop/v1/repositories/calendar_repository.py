from models.calendar import Calendar, CalendarPydantic
from middlewares import db_session_middleware

class CalendarRepository:
    
    def create_calendar(
        self, 
        data : CalendarPydantic,
        session : db_session_middleware
    ):
        calendar = Calendar()
        calendar.user_id = data.user_id
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
        user_id : str,
        session : db_session_middleware
    ):
        calendar = session.query(Calendar).filter(Calendar.user_id == user_id).first()
        return calendar