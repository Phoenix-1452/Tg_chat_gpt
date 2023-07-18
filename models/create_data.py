from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME
from models.model import User

engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}")

session = Session(bind=engine)


def registration(user_id):
    try:
        user = User(user_id=user_id)
        user.history = list
        session.add(user)
        session.commit()
    except Exception:
        pass


def buy_vip(user_id, days):
    user = session.query(User).filter_by(user_id=user_id).first()
    user.vip = True
    user.vip_days_left = days
    session.commit()


def prompts(user_id, history):
    user = session.query(User).filter_by(user_id=user_id).first()
    user.history = list(user.history)
    user.history.append(history)
    session.commit()


def get_history(user_id):
    user = session.query(User).filter_by(user_id=user_id).first()
    ans = user.history
    return ans


def clear_history(user_id):
    user = session.query(User).filter_by(user_id=user_id).first()
    user.history = []
    session.commit()


session.close()
