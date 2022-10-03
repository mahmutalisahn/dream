from array import array
import json
from typing import Any, Dict, List, Optional
from pydantic import BaseModel
from sqlalchemy import Column, String, Time, Date, Integer, Boolean, ARRAY
from base import Base
from helper import OrmHelper
from datetime import time, date

JSONObject = Dict[str, Any]

class SecureBooking(Base):
    __tablename__ = "secure_booking"
    __table_args__ = {"schema": "lapcalendar"}

    secure_password : str = Column(String)
    all_days : bool = Column(Boolean)
    available_dates : date = Column(ARRAY(date))
    user_id : str = Column(String)

    def __repr__(self) -> str:
        return json.dumps(self.dict())
    def __str__(self) -> str:
        return json.dumps(self.dict())
    def dict(self) -> dict:
        return OrmHelper.toDict(self)

class SecureBookingPydantic(BaseModel):
    secure_password : Optional[str]
    all_days : Optional[bool]
    available_dates : Optional[date]
    user_id : Optional[str]

    class Config:
        orm_mode = True
