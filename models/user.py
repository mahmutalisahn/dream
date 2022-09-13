import json
from typing import Any, Dict, Optional
from pydantic import BaseModel
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from base import Base
from helper import OrmHelper

JSONObject = Dict[str, Any]

class User(Base):
    __tablename__ = "user"
    __table_args__ = {"schema":"public"}
    user_id :str = Column(String, primary_key=True)
    email : str = Column(String, primary_key=True)
    username : str = Column(String, primary_key=True)
    password : str = Column(String)
    name :str = Column(String)
    surname : str = Column(String)
    phone : int = Column(Integer)

#    def __repr__(self) -> str:
#        return json.dumps(self.dict())

#    def __str__(self) -> str:
#        return json.dumps(self.dict())

#    def dict(self) -> dict:
#        return OrmHelper.toDict(self)

class UserPydantic(BaseModel):

    email : Optional[str]
    username : Optional[str]
    password : Optional[str]
    name : Optional[str]
    surname : Optional[str]
    phone : Optional[int]    

    class Config:
        orm_mode = True

