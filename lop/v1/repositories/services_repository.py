from middlewares import db_session_middleware
from models.service import  Service, ServicePydantic

import uuid

class ServiceRepository:
    
    def create_service(
        self, 
        data : ServicePydantic,
        session : db_session_middleware        
    ):
        service = Service()

        service.service_id = str(uuid.uuid1())        
        service.user_id = data.user_id
        service.service_name = data.service_name
        service.service_description = data.service_description
        service.service_price = data.service_price
        service.service_duration = data.service_duration

        session.add(service)
        session.commit()
        return service.service_id
    
    def get_service(
        self,
        user_id : str,
        session : db_session_middleware
    ):
        services = session.query(Service).filter(Service.user_id == user_id).all()
        return services
    
    def update_service(
        self,
        service_id : str,
        data : ServicePydantic,
        session : db_session_middleware
    ):

        service = session.query(Service).filter(Service.user_id == data.user_id, Service.service_id == service_id).first()

        if data.service_name != None:
            
            if data.service_description != None:
                
                if data.service_price != None:
                    
                    if data.service_duration != None:
                      #update service_name, service_description, service_price, service_duration
                        service.service_name = data.service_name
                        service.service_description = data.service_description
                        service.service_duration = data.service_duration
                        service.service_price = data.service_price
                        session.add(service)
                        session.commit()
                        return service.service_id
                    
                    else:
                        #update service_name, service_description, service_price
                        service.service_name = data.service_name
                        service.service_description = data.service_description
                        service.service_price = data.service_price
                        session.add(service)
                        session.commit()
                        return service.service_id
                else:
                    #update service_name, service_description
                    service.service_name = data.service_name
                    service.service_description = data.service_description
                    session.add(service)
                    session.commit()
                    return service.service_id

            else:
                #update service_name
                service.service_name = data.service_name
                session.add(service)
                session.commit()
                return service.service_id

        elif data.service_description != None:

            if data.service_price != None:
                
                if data.service_duration != None:
                    #service_description, service_price, service_duration
                    service.service_description = data.service_description
                    service.service_duration = data.service_duration
                    service.service_price = data.service_price
                    session.add(service)
                    session.commit()
                    return service.service_id
                else:
                    #service_description, service_price
                    service.service_description = data.service_description
                    service.service_price = data.service_price
                    session.add(service)
                    session.commit()
                    return service.service_id
            
            else:
                #service_description
                service.service_description = data.service_description
                session.add(service)
                session.commit()
                return service.service_id

        elif data.service_price != None:
                
            if data.service_duration != None:
                #update service_price, service_duration
                service.service_price = data.service_price
                service.service_duration = data.service_duration
                session.add(service)
                session.commit()
                return service.service_id

            else:
                #update service_price
                service.service_price = data.service_price
                session.add(service)
                session.commit()
                return service.service_id

        elif data.service_duration != None:
            #update service_duration
            service.service_duration = data.service_duration
            session.add(service)
            session.commit()
            return service.service_id
    
        else :
            return None

        
    def delete_service(
        self,
        user_id : str,
        service_id : str,
        session : db_session_middleware
    ):
        service = session.query(Service).filter(Service.user_id == user_id, Service.service_id == service_id).first()
        session.delete(service)
        session.commit()
        return service_id