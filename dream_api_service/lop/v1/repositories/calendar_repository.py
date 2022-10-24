# type: ignore
from models.calendar import Calendar, CalendarPydantic, CalendarSaverPydantic
from middlewares import db_session_middleware
from db import sqlalchemy_engine
import pandas as pd
from datetime import datetime, timedelta

notworking = "NotWorking_NotWorking_NotWorking_NotWorking"
nolaunch = "NoLaunch_NoLaunch"

class CalendarRepository:

    def create_calendar(
        self, 
        data : CalendarSaverPydantic,
        session : db_session_middleware
    ):

        calendar = Calendar()
        calendar.user_id = data.user_id

        if data.monday_not_working == True:
            calendar.monday = notworking
        else:
            new_end = datetime(100,1,1,data.monday_end.hour, data.monday_end.minute, data.monday_end.second) - timedelta(seconds=1)

            if data.monday_no_launch == True:
                calendar.monday = str(data.monday_start) + "_" + str(new_end.time()) + "_" + nolaunch    
            else :
                new_launch_end = datetime(100,1,1,data.monday_launch_end.hour, data.monday_launch_end.minute, data.monday_launch_end.second) - timedelta(seconds = 1) 
                calendar.monday = str(data.monday_start) + "_" + str(new_end.time()) + "_" + str(data.monday_launch_start) +   "_" + str(new_launch_end.time())

        if data.tuesday_not_working == True:
            calendar.tuesday = notworking
        else :
            new_end = datetime(100,1,1,data.tuesday_end.hour, data.tuesday_end.minute, data.tuesday_end.second) - timedelta(seconds=1) 

            if data.tuesday_no_launch == True:
                calendar.tuesday = str(data.tuesday_start) + "_" + str(new_end.time()) + "_" + nolaunch
            else:
                new_launch_end = datetime(100,1,1,data.tuesday_launch_end.hour, data.tuesday_launch_end.minute, data.tuesday_launch_end.second) - timedelta(seconds = 1)
                calendar.tuesday = str(data.tuesday_start) + "_" + str(new_end.time()) + "_" + str(data.monday_launch_start) + "_" + str(new_launch_end.time())

        if data.wednesday_not_working == True:
            calendar.wednesday = notworking
        else:
            new_end = datetime(100,1,1,data.wednesday_end.hour, data.wednesday_end.minute, data.wednesday_end.second) - timedelta(seconds=1) 

            if data.wednesday_no_launch == True:
                calendar.tuesday = str(data.tuesday_start) + "_" + str(new_launch_end.time()) + "_" + nolaunch
            else:
                new_launch_end = datetime(100,1,1,data.wednesday_launch_end.hour, data.wednesday_launch_end.minute, data.wednesday_launch_end.second) - timedelta(seconds = 1)
                calendar.wednesday = str(data.tuesday_start) + "_" + str(new_end.time()) + "_" + str(data.monday_launch_start) + "_" + str(new_launch_end.time())

        if data.thursday_not_working == True:
            calendar.thursday = notworking
        else:
            new_end = datetime(100,1,1,data.thursday_end.hour, data.thursday_end.minute, data.thursday_end.second) - timedelta(seconds=1) 

            if data.thursday_no_launch == True:
                calendar.thursday = str(data.thursday_start) + "_" + str(new_launch_end.time()) + "_" + nolaunch
            else:
                new_launch_end = datetime(100,1,1,data.thursday_launch_end.hour, data.thursday_launch_end.minute, data.thursday_launch_end.second) - timedelta(seconds = 1)
                calendar.thursday = str(data.thursday_start) + "_" + str(new_end.time()) + "_" + str(data.monday_launch_start) + "_" + str(new_launch_end.time())

        if data.friday_not_working == True:
            calendar.friday = notworking
        else:
            new_end = datetime(100,1,1,data.friday_end.hour, data.friday_end.minute, data.friday_end.second) - timedelta(seconds=1) 

            if data.friday_no_launch == True:
                calendar.friday = str(data.friday_start) + "_" + str(new_launch_end.time()) + "_" + nolaunch
            else:
                new_launch_end = datetime(100,1,1,data.friday_launch_end.hour, data.friday_launch_end.minute, data.friday_launch_end.second) - timedelta(seconds = 1)
                calendar.friday = str(data.friday_start) + "_" + str(new_end.time()) + "_" + str(data.monday_launch_start) + "_" + str(new_launch_end.time())

        if data.saturday_not_working == True:
            calendar.saturday = notworking
        else:
            new_end = datetime(100,1,1,data.saturday_end.hour, data.saturday_end.minute, data.saturday_end.second) - timedelta(seconds=1) 

            if data.saturday_no_launch == True:
                calendar.saturday = str(data.saturday_start) + "_" + str(new_launch_end.time()) + "_" + nolaunch
            else:
                new_launch_end = datetime(100,1,1,data.saturday_launch_end.hour, data.saturday_launch_end.minute, data.saturday_launch_end.second) - timedelta(seconds = 1)
                calendar.saturday = str(data.saturday_start) + "_" + str(new_end.time()) + "_" + str(data.monday_launch_start) + "_" + str(new_launch_end.time())

        if data.sunday_not_working == True:
            calendar.sunday = notworking
        else:
            new_end = datetime(100,1,1,data.sunday_end.hour, data.sunday_end.minute, data.sunday_end.second) - timedelta(seconds=1) 

            if data.sunday_no_launch == True:
                calendar.sunday = str(data.sunday_start) + "_" + str(new_launch_end.time()) + "_" + nolaunch
            else:
                new_launch_end = datetime(100,1,1,data.sunday_launch_end.hour, data.sunday_launch_end.minute, data.sunday_launch_end.second) - timedelta(seconds = 1)
                calendar.sunday = str(data.sunday_start) + "_" + str(new_end.time()) + "_" + str(data.monday_launch_start) + "_" + str(new_launch_end.time())

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


