# type: ignore

from fastapi.params import Depends

from interface.generic_router import GenericRouter
from middlewares import db_session_middleware

from models.service import Service, ServicePydantic
from lop.v1.service.service_service import ServiceService

class ServiceRouter(GenericRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.service_service = ServiceService()
        self.bind_routes()

    def bind_routes(self):
        self.get_router().get("/{user_id}")(self.get_service)
        self.get_router().put("/{service_id}")(self.update_service)
        self.get_router().post("/")(self.create_service)
        self.get_router().delete("/{user_id}/{service_id}")(self.delete_service)

    def create_service(
        self, 
        data : ServicePydantic = Depends(),
        session : db_session_middleware = Depends()
    ):  
        '''Service oluştur'''
        service = self.service_service.create_service(data, session)
        return service
    
    def get_service(
        self, 
        user_id : str,
        service_id : str,
        session : db_session_middleware = Depends()
    ):
        '''Service çek'''
        services = self.service_service.get_service(service_id, user_id, session)
        return services
    
    def update_service(
        self,
        service_id : str,
        data : ServicePydantic = Depends(),
        session : db_session_middleware = Depends()
    ):
        '''Service güncelle'''
        service = self.service_service.update_service(service_id, data, session)
        return service

    def delete_service(
        self,
        user_id : str,
        service_id : str,
        session : db_session_middleware = Depends()
    ):
        '''Service sil'''
        service = self.service_service.delete_service(user_id, service_id, session)
        return service