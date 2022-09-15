from middlewares import db_session_middleware
from models.booking import BookingPydantic
from ..repositories.booking_repository import BookingRepository

class BookingService:
    def __init__(self):
        self.booking_repository = BookingRepository()
    
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