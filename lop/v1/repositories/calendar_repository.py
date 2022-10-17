from models.calendar import Calendar, CalendarPydantic
from middlewares import db_session_middleware
from db import sqlalchemy_engine
import pandas as pd
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

        return calendar.user_id

    def get_calendar(
        self, 
        user_id : str,
        session : db_session_middleware
    ):
        calendar = session.query(Calendar).filter(Calendar.user_id == user_id).first()
        return calendar

    def update_calendar(
        self, 
        user_id : str,
        day : int,
        new_shift_details : str,
        session : db_session_middleware
    ):
        day = {
            1:"monday",
            2:"tuesday",
            3:"wednesday",
            4:"thursday",
            5:"friday",
            6:"saturday",
            7:"sunday"
        }
        calendar = session.query(Calendar).filter(Calendar.user_id == user_id)
        calendar.day[day] = new_shift_details
        session.add(calendar)
        session.commit()
        return calendar.user_id

    def get_user_calendar(
        self,
        user_id
    ):
        with sqlalchemy_engine.connect() as con:
            con.execution_options(isolation_level="AUTOCOMMIT")

            shift = con.execute("""
                SELECT
                    split_part(monday, '_', 1) as monday_start, split_part(monday, '_', 2) as monday_end, split_part(monday, '_', 3) as monday_launch_start, split_part(monday, '_', 4) as monday_launch_end,
                    split_part(tuesday, '_', 1) as tuesday_start, split_part(tuesday, '_', 2) as tuesday_end, split_part(tuesday, '_', 3) as tuesday_launch_start, split_part(tuesday, '_', 4) as tuesday_launch_end,
                    split_part(wednesday, '_', 1) as wednesday_start, split_part(wednesday, '_', 2) as wednesday_end, split_part(wednesday, '_', 3) as wednesday_launch_start, split_part(wednesday, '_', 4) as wednesday_launch_end,
                    split_part(thursday, '_', 1) as thursday_start, split_part(thursday, '_', 2) as thursday_end, split_part(thursday, '_', 3) as thursday_launch_start, split_part(thursday, '_', 4) as thursday_launch_end,
                    split_part(friday, '_', 1) as friday_start, split_part(friday, '_', 2) as friday_end, split_part(friday, '_', 3) as friday_launch_start, split_part(friday, '_', 4) as friday_launch_end,
                    split_part(saturday, '_', 1) as saturday_start, split_part(saturday, '_', 2) as saturday_end, split_part(saturday, '_', 3) as saturday_launch_start, split_part(saturday, '_', 4) as saturday_launch_end,
                    split_part(sunday, '_', 1) as sunday_start, split_part(sunday, '_', 2) as sunday_end, split_part(sunday, '_', 3) as sunday_launch_start, split_part(sunday, '_', 4) as sunday_launch_end
                FROM lapcalendar.calendar
                WHERE user_id = '{}';
            """.format(user_id)
            )
            df = pd.DataFrame(shift, columns=[
                'monday_start', 'monday_end', 'monday_launch_start', 'monday_launch_end', 
                'tuesday_start', 'tuesday_end', 'tuesday_launch_start', 'tuesday_launch_end', 
                'wednesday_start', 'wednesday_end', 'wednesday_launch_start', 'wednesday_launch_end', 
                'thursday_start', 'thursday_end', 'thursday_launch_start', 'thursday_launch_end',
                'friday_start', 'friday_end', 'friday_launch_start', 'friday_launch_end',
                'saturday_start', 'saturday_end', 'saturday_launch_start', 'saturday_launch_end', 
                'sunday_start', 'sunday_end', 'sunday_launch_start', 'sunday_launch_end'])


        return df
