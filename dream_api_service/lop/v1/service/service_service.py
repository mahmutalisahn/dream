# type: ignore

from middlewares import db_session_middleware
from models.service import Service, ServicePydantic
from lop.v1.repositories.services_repository import ServiceRepository

class ServiceService:
    def __init__(self) -> None:
        self.service_repository = ServiceRepository()
    
    def create_service(
        self, 
        data : ServicePydantic,
        session : db_session_middleware
    ):
        service = self.service_repository.create_service(data, session)
        return service
    
    def get_service(
        self, 
        user_id,
        service_id : str,
        session : db_session_middleware
    ):
        service = self.service_repository.get_service(service_id, user_id, session)
        return service
    
    def update_service(
        self, 
        service_id : str,
        data : ServicePydantic,
        session : db_session_middleware
    ):
        service = self.service_repository.update_service(service_id, data, session)
        return service
    
    def delete_service(
        self, 
        user_id : str,
        service_id : str,
        session : db_session_middleware
    ):
        service = self.service_repository.delete_service(user_id, service_id, session)
        return service