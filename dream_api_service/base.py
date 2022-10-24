from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base

metadata_obj = MetaData(schema="lapcalendar")

Base = declarative_base(metadata=metadata_obj)
