from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, TIMESTAMP, JSON, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    balance = Column(Float, default=0, nullable=False)
    vip = Column(Boolean, default=False, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    history = Column(JSON)





