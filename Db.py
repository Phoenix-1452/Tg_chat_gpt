from sqlalchemy import create_engine, MetaData, Column, Integer, BigInteger, Float
from sqlalchemy.orm import Session, DeclarativeBase
import Secret

class User_info:
    pass
        

engine = create_engine(f"postgresql+psycopg2://postgres:{Secret.password}@localhost/Users")
session = Session(bind=engine)

class Base(DeclarativeBase):
    pass
class User(Base):
    __tablename__ = "User_info"

    User_id = Column(Integer, primary_key=True)
    Telegram_id = Column(BigInteger)
    Day_of_join = Column(Integer)
    Balance = Column(Float)
    Vip_status = Column(Integer)

c1 = User(
    Balance = 10)

session.add(c1)
session.commit()
