from models.booking import Booking, BookingPydantic
from middlewares import db_session_middleware

import uuid

class BookingRepository:
    
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
        booking.end_book = data.end_book
        booking.date = data.date
        booking.status = 0

        session.add(booking)
        session.commit()
        return booking.dict()
    
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
    
