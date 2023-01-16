from middlewares import db_session_middleware
from models.booking import BookingPydantic
from ..repositories.booking_repository import BookingRepository

class BookingService:
    def __init__(self):
        self.booking_repository = BookingRepository()
    
    def service_status(
        self,
        session : db_session_middleware
    ):
        status = self.booking_repository.get_all(session)
        return len(status)

    def admin(
        self,
        session : db_session_middleware
    ):
        books = self.booking_repository.admin(session)
        return books

    def create_booking(
        self,
        data : BookingPydantic,
        session : db_session_middleware
    ):
        booking = self.booking_repository.create_booking(data, session)
        return booking
    
    def get_booking(
        self,
        user_id : str,
        session : db_session_middleware
    ):
        bookings = self.booking_repository.get_booking(user_id, session)
        return bookings
 
    def get_valid_booking(
        self,
        user_id : str,
        session : db_session_middleware
    ):
        bookings = self.booking_repository.get_valid_booking(user_id, session)
        return bookings

    def get_invalid_booking(
        self,
        user_id : str,
        session : db_session_middleware
    ):
        bookings = self.booking_repository.get_invalid_booking(user_id, session)
        return bookings

    def confirm_booking(
        self,
        user_id : str,
        booking_id : str,
        session : db_session_middleware
    ):
        booking_id = self.booking_repository.confirm_booking(user_id, booking_id, session)
        return booking_id
    
    def get_booking_of_day(
        self,
        user_id : str,
        date,
    ):
        bookings = self.booking_repository.get_booking_of_day(user_id, date)
        return bookings