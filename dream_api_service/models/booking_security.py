import json
from typing import Any, Dict, Optional
from pydantic import BaseModel
from sqlalchemy import Column, String, Time, Date, Integer
from dream_api_service.base import Base
from dream_api_service.helper import OrmHelper
from datetime import time, date

JSONObject = Dict[str, Any]

class BookingSecurity(Base):

    __tablename__ = "booking_security"
    __table_args__ = {"schema": "lapcalendar"}

    booking_security_id : str = Column(String, primary_key=True)
    booking_id :str = Column(String)
    customer_ssn : str = Column(String)

    def __repr__(self) -> str:
        return json.dumps(self.dict())
    def __str__(self) -> str:
        return json.dumps(self.dict())
    def dict(self) -> dict:
        return OrmHelper.toDict(self)
