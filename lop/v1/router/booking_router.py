from fastapi.params import Depends

from interface.generic_router import GenericRouter
from middlewares import db_session_middleware

from models.booking import Booking, BookingPydantic
from lop.v1.service.booking_servce import BookingService

class BookingRouter(GenericRouter):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.booking_service = BookingService()
        self.bind_routes()
    
    def bind_routes(self):
        self.get_router().get("/{user_id}")(self.get_booking)
        self.get_router().get("/valid/{user_id}")(self.get_valid_booking)
        self.get_router().get("/invalid/{user_id}")(self.get_invalid_booking)
        self.get_router().get("/confirm/{user_id}/{booking_id}")(self.confirm_booking)
        self.get_router().post("/")(self.create_booking)

    def create_booking(
        self,
        data : BookingPydantic = Depends(),
        session : db_session_middleware = Depends(),
    ):
        booking_id = self.booking_service.create_booking(data, session)
        return booking_id
    
    def get_booking(
        self,
        user_id : str,
        session : db_session_middleware = Depends()
    ):
        bookings = self.booking_service.get_booking(user_id, session)
        return bookings

    def get_valid_booking(
        self,
        user_id : str,
        session : db_session_middleware = Depends()
    ):
        bookings = self.booking_service.get_valid_booking(user_id, session)
        return bookings

    def get_invalid_booking(
        self,
        user_id : str,
        session : db_session_middleware = Depends()
    ):
        bookings = self.booking_service.get_invalid_booking(user_id, session)
        return bookings

    def confirm_booking(
        self,
        user_id : str,
        booking_id : str,
        session : db_session_middleware = Depends()
    ):
        booking_id = self.booking_service.confirm_booking(user_id, booking_id, session)
        return booking_id