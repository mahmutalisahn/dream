
from random import SystemRandom
from models.booking import Booking
from models.user import UserPydantic, User
from middlewares import db_session_middleware
from db import sqlalchemy_engine
import uuid

class UserRepository:

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
        user_id : str,
        month : int,
        session : db_session_middleware
    ):  
        #create month
        month_start, month_end = self.create_month(month)
        
        user = self.get_user_by_id(user_id, session)

        with sqlalchemy_engine.connect() as con:
            con.execution_options(isolation_level="AUTOCOMMIT")
            result = con.execute(
                """
                select
                    to_char(dd::date, 'MM-DD') da,
                    case
                         when
                            exists(
                                SELECT u.date_list::varchar
                                FROM lapcalendar.user u
                                WHERE u.user_id LIKE '{}'
                                    AND dd::date = ANY (u.date_list)
                            )
                        then 'çalışmıyor'
                        when
                            exists(
                                SELECT x::time time
                                    FROM
                                        generate_series(dd,
                                                        dd,
                                                        interval  '1 hour') x

                                    WHERE
                                        x::time not in (
                                            SELECT distinct start_book from lapcalendar.bookings where date=dd::date AND user_id = '{}'
                                        )
                            )
                        then 'müsait'
                        else 'dolu' end

                from generate_series
                 ( '{} {}'::timestamp
                 , '{} {}'::timestamp
                 , '1 day'::interval) dd;

                """.format(user_id, user_id, month_start, user.shift_start, month_end, user.shift_end)
            )

        return result.all()

    def get_calendar_day(
        self,
        user_id : str,
        date : str,
        session : db_session_middleware
    ):
        user = self.get_user_by_id(user_id, session)

        with sqlalchemy_engine.connect() as con:
            con.execution_options(isolation_level="AUTOCOMMIT")
            result = con.execute(
                """
                   SELECT x::time time, case when  x::time not in (
                                            SELECT distinct start_book from lapcalendar.bookings where date='{}'::date and user_id = '{}'
                                        ) then 'boş' else 'dolu' end
                                    FROM
                                        generate_series('{} {}',
                                                        '{} {}',
                                                        interval  '1 hour') x

                                        
                """.format(date, user_id, date, user.shift_start, date, user.shift_end)
            )

        return result.all()

    def create_month(
        self,
        month
    ):

        if month == 1:
            month_start = '2022-01-01'
            month_end = '2022-01-31'
        elif month == 2:
            month_start = '2022-02-01'
            month_end = '2022-02-28'
        elif month == 3:
            month_start = '2022-03-01'
            month_end = '2022-03-31'
        elif month == 4:
            month_start = '2022-04-01'
            month_end = '2022-04-30'
        elif month == 5:
            month_start = '2022-05-01'
            month_end = '2022-05-31'
        elif month == 6:
            month_start = '2022-06-01'
            month_end = '2022-06-30'
        elif month == 7:
            month_start = '2022-07-01'
            month_end = '2022-07-31'
        elif month == 8:
            month_start = '2022-08-01'
            month_end = '2022-08-31'
        elif month == 9:
            month_start = '2022-09-01'
            month_end = '2022-09-30'
        elif month == 10:
            month_start = '2022-10-01'
            month_end = '2022-10-31'
        elif month == 11:
            month_start = '2022-11-01'
            month_end = '2022-11-30'
        elif month == 12:
            month_start = '2022-12-01'
            month_end = '2022-12-31'


        return month_start, month_end