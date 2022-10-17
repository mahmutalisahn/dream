# type: ignore
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
    
    user_id: str = Column(String, primary_key=True)
    monday: str = Column(String)
    tuesday: str = Column(String)
    wednesday: str = Column(String)
    thursday: str = Column(String)
    friday: str = Column(String)
    saturday: str = Column(String)
    sunday: str = Column(String)

    def __repr__(self) -> str:
        return json.dumps(self.dict())
    def __str__(self) -> str:
        return json.dumps(self.dict())
    def dict(self) -> dict:
        return OrmHelper.toDict(self)


class CalendarPydantic(BaseModel):

    user_id : Optional[str]
    monday : Optional[str]
    tuesday : Optional[str]
    wednesday : Optional[str]
    thursday : Optional[str]
    friday : Optional[str]
    saturday : Optional[str]
    sunday : Optional[str]

    class Config:
        orm_mode = True
