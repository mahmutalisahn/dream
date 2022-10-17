from calendar import Calendar
from typing import List
from datetime import datetime, timedelta

from db import sqlalchemy_engine

from middlewares import db_session_middleware

from models.booking import Booking
from models.portfolio import Portfolio, PortfolioPydantic
from models.user import UserPydantic, User

from ..utils import generate_time

from .services_repository import ServiceRepository
from .booking_repository import BookingRepository
from .calendar_repository import CalendarRepository

import uuid
import pandas as pd
import time
class UserRepository:
    
    def __init__(self):
        self.service_repository = ServiceRepository()
        self.booking_repository = BookingRepository()
        self.calendar_repository = CalendarRepository()

    def get_user_by_id(
        self,
        user_id : str,
        session : db_session_middleware
    ):
        user = session.query(User).filter(User.user_id == user_id).first()
        return user

    def get_user_by_username(
        self,
        username : str,
        session : db_session_middleware
    ):
        user = session.query(User).filter(User.username == username).first()
        return user

    def create_user(
        self,
        data = UserPydantic,
        session = db_session_middleware
    ):
    
        user = User()
        user.email = data.email
        user.username = data.username
        user.name = data.name
        user.surname = data.surname
        user.user_id = str(uuid.uuid1())
        user.password = data.password
        
        if data.phone != None:
            user.phone = data.phone

        session.add(user)
        session.commit()

        return user.username

    def update_user(
        self,
        user_id : str,
        data : UserPydantic,
        update : List[str],
        session : db_session_middleware
    ):
        user = session.query(User).filter(User.user_id == user_id).first()

        for make_update in update:
            if make_update == "username":
                pass
            elif make_update == "password":
                pass
            elif make_update == "email":
                pass
            elif make_update == "phone":
                pass
            elif make_update == "name":
                pass
            elif make_update == "surname":
                pass

    def create_portfolio(
        self,
        user_id,
        data = PortfolioPydantic,
        session = db_session_middleware
    ):
        portfolio = Portfolio()

        portfolio.user_id = user_id
        portfolio.title = data.title
        portfolio.description = data.description

        session.add(portfolio)
        session.commit()

        return 

    def update_portfolio(
        self,
        user_id : str,
        update : List[str],
        data : PortfolioPydantic,
        session : db_session_middleware
    ):

        portfolio = session.query(Portfolio).filter(Portfolio.user_id == user_id).first()

        for make_update in update:
            if make_update == "title":
                portfolio.title = data.title
            elif make_update == "description":
                portfolio.description = data.description

        session.add(portfolio)
        session.commit()

        return "done"

    def delete_portfolio(
        self,
        user_id : str,
        session : db_session_middleware
    ):
        portfolio = session.query(Portfolio).filter(Portfolio.user_id == user_id).first()
        session.delete(portfolio)
        session.commit()

        return "done"


    def check(
        self,
        username : str,
        password : str,
        session : db_session_middleware
    ):
        user = self.get_user_by_username(username, session)
        
        if user is not None:
            if user.password == password:
                return user

        return False

    def get_calendar_month(
        self,
        service_id : str,
        user_id : str,
        year : str,
        month : str,
        session : db_session_middleware
    ):  

        dates = []
        time_limit = self.create_month(month)
        
        counter = 1
        while(counter <= time_limit):
            date = '{}-{}-{}'.format(year, month, counter)

            if self.get_calendar_day( service_id, user_id, date, session) != []:
                dates.append(counter)
            
            counter += 1
            
        return dates
        
    def get_calendar_day(
        self,
        service_id : str,
        user_id : str,
        date : str,
        session : db_session_middleware
    ):
        service = self.service_repository.get_service(service_id,session)
        duration = service[0].service_duration

        df = self.calendar_repository.get_user_calendar(user_id)
        #kullanıcının çalışma şeklini al   
        day = datetime(2022, 2, 10, 1, 0, 0).weekday()     
        weekday = self.get_weekday(int(day))
        #baktığın günün adını bul
        #kullanıcının çalışma saatlerini çıkar
        shift_start = df.iloc[0]['{}_start'.format(weekday)]
        shift_end = df.iloc[0]['{}_end'.format(weekday)]
        launch_start = df.iloc[0]['{}_launch_start'.format(weekday)]
        launch_end = df.iloc[0]['{}_launch_end'.format(weekday)]
    
        with sqlalchemy_engine.connect() as con:

            con.execution_options(isolation_level="AUTOCOMMIT")
            result = con.execute(
                """
                    SELECT x::time time                    
                    FROM
                        generate_series('{} {}',
                                        '{} {}',
                                        interval  '15 min') x
                    WHERE x::time not in
                                (
                                    SELECT distinct start_book from lapcalendar.bookings where date='{}'::date and user_id = '{}' and status = 1
                                )
                                and
                                x::time not between '{}' and '{}'
                                and
                                x::time not in
                                (
                                    SELECT distinct start_book
                                    from lapcalendar.bookings
                                    where user_id = '{}' and date = '{}' and status = 1
                                )
                                
          
                    """.format(date, shift_start, date, shift_end, date, user_id, launch_start, launch_end, user_id, date)                                
            )
        
        result = result.all()
        return_result = []
        
        new_result = [datetime(100,1,1,r[0].hour, r[0].minute, r[0].second) for r in result]
        flag = False

        for r in new_result:
            new_r = r
            counter = int(duration)/15 
            while counter > 0:
                new_r += timedelta(seconds=900)
                if new_r in new_result:
                    flag = True
                    
                else:
                    flag = False
                    break
                counter -= 1
            
            if flag:
                return_result.append(r.time())
        return return_result

    def create_month(
        self,
        month
    ):
        if month == '01':
            day = 31
        elif month == '02':
            day = 28
        elif month == '03':
            day = 31
        elif month == '04':
            day = 30
        elif month == '05':
            day = 31
        elif month == '06':
            day = 30
        elif month == '07':
            day = 31
        elif month == '08':
            day = 31
        elif month == '09':
            day = 30
        elif month == '10':
            day = 31
        elif month == '11':
            day = 30
        elif month == '12':
            day = 31
        else :
            day = 0
        return day    

    def get_weekday(self, weekday):
        
        if weekday == 0:
            return'monday'
        elif weekday == 1:
            return'tuesday'
        elif weekday == 2:
            return'wednesday'
        elif weekday == 3:
            return'thursday'
        elif weekday == 4:
            return'friday'
        elif weekday == 5:
            return'saturday'
        elif weekday == 6:
            return'sunday'

