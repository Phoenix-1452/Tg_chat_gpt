from sqlalchemy import create_engine, MetaData, Column, Integer, BigInteger, Float, DateTime, TIMESTAMP, select
from sqlalchemy.orm import Session, DeclarativeBase
import psycopg2
from datetime import datetime

class User_info:
    pass
        
conn = psycopg2.connect(dbname="Users", user='postgres', password='KlimKva22', host='localhost')
engine = create_engine(f"postgresql+psycopg2://postgres:KlimKva22@localhost/Users")

cursor = conn.cursor()
session = Session(bind=engine)
cursor.execute('SELECT "User_id" FROM "User_info" WHERE "Telegram_id" = 10')
all_users = cursor.fetchall()
print(all_users)

class Base(DeclarativeBase):
    pass
class User(Base):
    __tablename__ = "User_info"

    User_id = Column(Integer, primary_key=True)
    Telegram_id = Column(BigInteger)
    Day_of_join = Column(TIMESTAMP, default=datetime.utcnow)
    Balance = Column(Float)
    Vip_status = Column(TIMESTAMP, default=datetime.utcnow)

def registration(Telegram_id, Balance):
    c1 = User(
        Telegram_id = Telegram_id,
        Balance = Balance)
    session.add(c1)
    session.commit()

#registration(Telegram_id = 10, Balance = 20)
#xyi = session.query(User).all()
#print(xyi[4].Telegram_id)
