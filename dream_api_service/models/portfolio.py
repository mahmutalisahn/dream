from io import StringIO
import json
from typing import Any, Dict, Optional
from pydantic import BaseModel
from sqlalchemy import Column, String, Time, Date, Integer
from base import Base
from helper import OrmHelper
from datetime import time, date

JSONObject = Dict[str, Any]

class Portfolio(Base):
    __tablename__ = "portfolio"
    __table_args__ = {"schema": "public"}

    user_id : str = Column(String, primary_key=True)
    title : str = Column(String)
    description : str = Column(String)

    def __repr__(self) -> str:
        return json.dumps(self.dict())
    def __str__(self) -> str:
        return json.dumps(self.dict())
    def dict(self) -> dict:
        return OrmHelper.toDict(self)

class PortfolioPydantic(BaseModel):

    title : Optional[str]
    description : Optional[str]
    class Config:
        orm_mode = True
