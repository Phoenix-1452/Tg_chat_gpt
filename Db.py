from sqlalchemy import create_engine, MetaData, Column, Integer, BigInteger, Float, DateTime
from sqlalchemy.orm import Session, DeclarativeBase
import Secret

class User_info:
    pass
        

engine = create_engine(f"postgresql+psycopg2://postgres:KlimKva22@localhost/Users")
session = Session(bind=engine)

class Base(DeclarativeBase):
    pass
class User(Base):
    __tablename__ = "User_info"

    User_id = Column(Integer, primary_key=True)
    Telegram_id = Column(BigInteger)
    Day_of_join = Column(DateTime)
    Balance = Column(Float)
    Vip_status = Column(Integer)

c1 = User(
    Telegram_id = 3254513433,
    Day_of_join = "2023-12-23 02:14:14",
    Balance = 10.15)

session.add(c1)
session.commit()
