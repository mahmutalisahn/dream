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

        session.add(booking)
        session.commit()
        return booking.booking_id

    def get_booking(
        self,
        user_id,
        session : db_session_middleware
    ):
        bookings = session.query(Booking).filter(Booking.user_id == user_id).all()
        return bookings