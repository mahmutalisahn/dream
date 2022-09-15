import json
from typing import Any, Dict, Optional
from pydantic import BaseModel
from sqlalchemy import Column, String, Time
from base import Base
from helper import OrmHelper
from datetime import time 

JSONObject = Dict[str, Any]

class Booking(Base):
    __tablename__ = "bookings"
    __table_args__ = {"schema": "public"}

    booking_id :str = Column(String, primary_key=True)
    user_id : str = Column(String)
    customer_email : str = Column(String)
    customer_name : str = Column(String)
    customer_surname : str = Column(String)
    customer_phone : str = Column(String)
    start_book : time = Column(Time)
    end_book : time = Column(Time)

    def __repr__(self) -> str:
        return json.dumps(self.dict())
    def __str__(self) -> str:
        return json.dumps(self.dict())
    def dict(self) -> dict:
        return OrmHelper.toDict(self)

class BookingPydantic(BaseModel):
    user_id : Optional[str]
    customer_email : Optional[str]
    customer_name : Optional[str]
    customer_surname : Optional[str]
    customer_phone : Optional[str]
    start_book : Optional[time]
    end_book : Optional[time]
    
    class Config:
        orm_mode = True