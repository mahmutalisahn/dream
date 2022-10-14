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
    __tablename__ = "exceptional_days"
    __table_args__ = {"schema": "lapcalendar"}
    user_id: str = Column(String, primary_key=True)
    exceptional_date : date = Column(Date)
    shift : str = Column(String)

    def __repr__(self) -> str:
        return json.dumps(self.dict())
    def __str__(self) -> str:
        return json.dumps(self.dict())
    def dict(self) -> dict:
        return OrmHelper.toDict(self)

class TimeSlotsPydantic(BaseModel):

    user_id : Optional[str]
    exceptional_date : Optional[date]
    shift : Optional[str]

    class Config:
        orm_mode = True
