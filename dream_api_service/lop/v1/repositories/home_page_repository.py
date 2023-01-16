from dream_api_service.db import sqlalchemy_engine
from dream_api_service.models.preview import Preview

from dream_api_service.middlewares import db_session_middleware
from .services_repository import ServiceRepository
import uuid
from datetime import datetime,timedelta,time
from .user_repository import UserRepository


class HomePageRepository:
    
    def __init__(self):
        self.service_repository = ServiceRepository()
        self.user_repository = UserRepository()

    def get_home(
        self,
        session : db_session_middleware
    ):
        list_of_cards = []
        
        pass