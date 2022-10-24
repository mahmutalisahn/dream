from code import interact
import json
from typing import Any, Dict, Optional
from pydantic import BaseModel
from sqlalchemy import Column, String, Time, Date, Integer
from dream_api_service.base import Base
from dream_api_service.helper import OrmHelper
from datetime import time, date

JSONObject = Dict[str, Any]

class Service(Base):
    __tablename__ = "service"
    __table_args__ = {"schema": "lapcalendar"}

    service_id = Column(String, primary_key=True)
    user_id = Column(String)
    service_name = Column(String)
    service_description = Column(String)
    service_price = Column(Integer)
    service_duration = Column(Integer)

    def __repr__(self) -> str:
        return json.dumps(self.dict())
    def __str__(self) -> str:
        return json.dumps(self.dict())
    def dict(self) -> dict:
        return OrmHelper.toDict(self)

class ServicePydantic(BaseModel):
    user_id : Optional[str]
    service_name : Optional[str]
    service_description : Optional[str]
    service_price : Optional[int]
    service_duration : Optional[int]

    class Config:
        orm_mode = True
