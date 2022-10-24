from typing import Optional
from fastapi.params import Depends

from dream_api_service.interface.generic_router import GenericRouter
from dream_api_service.middlewares import db_session_middleware

from dream_api_service.models.booking import Booking, BookingPydantic
from dream_api_service.lop.v1.service.booking_service import BookingService

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
        self.get_router().get("/day/{user_id}/{date}")(self.get_booking_of_day)
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
        user_id : Optional[str],
        session : db_session_middleware = Depends()
    ):
        bookings = self.booking_service.get_booking(user_id, session)
        return bookings

    def get_valid_booking(
        self,
        user_id : str,
        session : db_session_middleware = Depends()
    ):     
        '''Validate edilmiş bookingleri verir'''
        bookings = self.booking_service.get_valid_booking(user_id, session)
        return bookings

    def get_invalid_booking(
        self,
        user_id : str,
        session : db_session_middleware = Depends()
    ):
        '''Validate edilmemiş bookingleri verir'''
        bookings = self.booking_service.get_invalid_booking(user_id, session)
        return bookings

    def confirm_booking(
        self,
        user_id : str,
        booking_id : str,
        session : db_session_middleware = Depends()
    ):
        '''verilen user_id ve booking i onaylar, booking artık onaylanmışlar arasında yer alır'''
        booking_id = self.booking_service.confirm_booking(user_id, booking_id, session)
        return booking_id
    
    def get_booking_of_day(
        self, 
        user_id : str, 
        date : str, 
    ):
        '''Verilen tarihteki onaylanmış bookinglerin saatlerini verir'''
        booking_id = self.booking_service.get_booking_of_day(user_id, date)    
        return booking_id