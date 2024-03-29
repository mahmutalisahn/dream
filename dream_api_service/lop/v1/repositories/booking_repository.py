from db import sqlalchemy_engine
from models.booking import Booking, BookingPydantic
from models.booking_security import BookingSecurity
from sqlalchemy import func, desc

from middlewares import db_session_middleware
from .services_repository import ServiceRepository
import uuid
from datetime import datetime,timedelta,time
from .user_repository import UserRepository

class BookingRepository:
    
    def __init__(self):
        self.service_repository = ServiceRepository()
        self.user_repository = UserRepository()

    def get_all(
        self,
        session : db_session_middleware
    ):
        books = session.query(Booking).all()
        return books

    def admin(
        self,
        session : db_session_middleware
    ):
        books = session.query(Booking).all()
        return books

    def create_booking(
        self,
        data : BookingPydantic,
        session : db_session_middleware
    ):
            
        booking = Booking()
        booking.booking_id = str(uuid.uuid1())
        booking.user_id = data.user_id
        booking.customer_email = data.customer_email
        booking.customer_name = data.customer_name
        booking.customer_surname = data.customer_surname
        booking.customer_phone = data.customer_phone
        booking.start_book = data.start_book
        booking.date = data.date
        booking.service_id = data.service_id
        booking.status = 0


        service = self.service_repository.get_service(data.service_id, data.user_id, session)       
        
        duration = service.service_duration
        print(duration)

        end_book = datetime(100,1,1,data.start_book.hour, data.start_book.minute, data.start_book.second)
        end_book += timedelta(minutes=duration)
        booking.end_book = end_book

        session.add(booking)

        session.commit()
        return booking
    
    def get_booking(
        self,
        user_id,
        session : db_session_middleware
    ):
        bookings = session.query(Booking).filter(Booking.user_id == user_id).all()
        return bookings

    def get_valid_booking(
        self,
        user_id,
        session : db_session_middleware
    ):
        bookings = session.query(Booking).filter(Booking.user_id == user_id, Booking.status == 1).all()
        return bookings

    def get_invalid_booking(
        self,
        user_id,
        session : db_session_middleware
    ):
        bookings = session.query(Booking).filter(Booking.user_id == user_id, Booking.status == 0).all()
        return bookings

    def confirm_booking(
        self,
        user_id : str,
        booking_id : str,
        session : db_session_middleware
    ):
        test_booking = session.query(Booking)\
            .filter(Booking.user_id == user_id, Booking.booking_id == booking_id).first()

        control_date = session.query(Booking)\
            .filter(Booking.user_id == user_id, Booking.date == test_booking.date, Booking.start_book == test_booking.start_book, Booking.status == 1)

        if control_date != None:
            return "Date is already booked"

        session.query(Booking)\
            .filter(Booking.user_id == user_id, Booking.booking_id == booking_id)\
                .update({Booking.status : 1})
        
        session.commit()

        return booking_id
    
    def get_booking_of_day(
        self,
        user_id,
        date,
    ):
        with sqlalchemy_engine.connect() as con:
            con.execution_options(isolation_level="AUTOCOMMIT")
            result = con.execute(
                """
                    SELECT start_book::varchar, end_book::varchar FROM lapcalendar.bookings WHERE user_id = '{}' AND date = '{}' AND status = 1;
                """.format(user_id, date)
            )
            
        return result.all()
    
