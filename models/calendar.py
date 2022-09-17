import json
from typing import Any, Dict, Optional
from pydantic import BaseModel
from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from datetime import date
from base import Base
from helper import OrmHelper

JSONObject = Dict[str, Any]

class Calendar(Base):
    __tablename__ = "calendar"
    __table_args__ = {"schema": "lapcalendar"}
    service_id: str = Column(String, primary_key=True)
    user_name : str = Column(String)
    monday: int = Column(Integer)
    tuesday: int = Column(Integer)
    wednesday: int = Column(Integer)
    thursday: int = Column(Integer)
    friday: int = Column(Integer)
    saturday: int = Column(Integer)
    sunday: int = Column(Integer)
    start_date: date = Column(Date)
    end_date: date = Column(Date)

    def __repr__(self) -> str:
        return json.dumps(self.dict())
    def __str__(self) -> str:
        return json.dumps(self.dict())
    def dict(self) -> dict:
        return OrmHelper.toDict(self)


class CalendarPydantic(BaseModel):

    service_id : Optional[str]
    user_name : Optional[str]
    monday : Optional[str]
    tuesday : Optional[str]
    wednesday : Optional[str]
    thursday : Optional[str]
    friday : Optional[str]
    saturday : Optional[str]
    sunday : Optional[str]
    start_date : Optional[date]
    end_date : Optional[date]

    class Config:
        orm_mode = True
