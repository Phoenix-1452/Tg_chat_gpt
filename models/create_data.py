from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME
from models.model import User
from datetime import datetime, timedelta, date


engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}")

session = Session(bind=engine)


def registration(user_id):
    try:
        user = User(user_id=user_id)
        user.history = list()
        session.add(user)
        session.commit()
    except Exception:
        pass


def buy_vip(user_id):
    try:
        user = session.query(User).filter_by(user_id=user_id).first()
        user.vip = True
        current_datetime = date.today()
        duration = timedelta(days=30)
        end_datetime = current_datetime + duration
        end_date_formatted = end_datetime.strftime('%Y-%m-%d')
        user.vip_days_left = end_date_formatted
        # print(end_date_formatted)
        session.commit()
    except Exception:
        pass


def prompts(user_id, history):
    try:
        user = session.query(User).filter_by(user_id=user_id).first()
        user.history = list(user.history)
        user.history.append(history)
        session.commit()
    except Exception:
        pass


def get_history(user_id):
    try:
        user = session.query(User).filter_by(user_id=user_id).first()
        ans = user.history
        return ans
    except Exception:
        pass


def clear_history(user_id):
    try:
        user = session.query(User).filter_by(user_id=user_id).first()
        user.history = list()
        session.commit()
    except Exception:
        pass


session.close()
