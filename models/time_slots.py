import json
from datetime import time
from typing import Any, Dict, Optional
from pydantic import BaseModel
from sqlalchemy import Column, String, Integer, Date, Time
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from datetime import date
from base import Base
from helper import OrmHelper


JSONObject = Dict[str, time, Any]

class TimeSlots(Base):
    __tablename__ = "time_slots"
    __table_args__ = {"schema": "public"}
    service_id: str = Column(String, primary_key=True)
    start_time : time = Column(Time)
    end_time : time = Column(Time)
    user_id : str = Column(String)

    def __repr__(self) -> str:
        return json.dumps(self.dict())
    def __str__(self) -> str:
        return json.dumps(self.dict())
    def dict(self) -> dict:
        return OrmHelper.toDict(self)

class TimeSlotsPydantic(BaseModel):

    service_id : Optional[str]
    start_time : Optional[time]
    end_time : Optional[time]
    user_id : Optional[str]

    class Config:
        orm_mode = True
