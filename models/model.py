from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, TIMESTAMP, JSON, Float, ARRAY, TEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False, unique=True)
    username = Column(String)
    balance = Column(Float, default=0, nullable=False)
    vip = Column(Boolean, default=False, nullable=False)
    vip_days_left = Column(Integer)
    history = Column(JSON, default=False)





