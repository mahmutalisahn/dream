# type: ignore
import json
from typing import Any, Dict, Optional
from pydantic import BaseModel
from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from datetime import date, timedelta, time
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

class CalendarSaverPydantic(BaseModel):

    user_id : Optional[str]
    
    monday_start : Optional[time]
    monday_end : Optional[time]
    monday_launch_start : Optional[time]
    monday_launch_end : Optional[time]
    monday_no_launch : Optional[bool]
    monday_not_working : Optional[bool]

    tuesday_start : Optional[time]
    tuesday_end : Optional[time]
    tuesday_launch_start : Optional[time]
    tuesday_launch_end : Optional[time]
    tuesday_no_launch : Optional[bool]
    tuesday_not_working : Optional[bool]

    wednesday_start : Optional[time]
    wednesday_end : Optional[time]
    wednesday_launch_start : Optional[time]
    wednesday_launch_end : Optional[time]
    wednesday_no_launch : Optional[bool]
    wednesday_not_working : Optional[bool]

    thursday_start : Optional[time]
    thursday_end : Optional[time]
    thursday_launch_start : Optional[time]
    thursday_launch_end : Optional[time]
    thursday_no_launch : Optional[bool]
    thursday_not_working : Optional[bool]

    friday_start : Optional[time]
    friday_end : Optional[time]
    friday_launch_start : Optional[time]
    friday_launch_end : Optional[time]
    friday_no_launch : Optional[bool]
    friday_not_working : Optional[bool]

    saturday_start : Optional[time]
    saturday_end : Optional[time]
    saturday_launch_start : Optional[time]
    saturday_launch_end : Optional[time]
    saturday_no_launch : Optional[bool]
    saturday_not_working : Optional[bool]

    sunday_start : Optional[time]
    sunday_end : Optional[time]
    sunday_launch_start : Optional[time]
    sunday_launch_end : Optional[time]
    sunday_no_launch : Optional[bool]
    sunday_not_working : Optional[bool]
