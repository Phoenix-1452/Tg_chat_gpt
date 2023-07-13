from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model import User
from config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME

# Создание подключения к базе данных
engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}")

session = Session(bind=engine)


class Registration:

    def __init__(self, username):
        self.username = username
        user = User(username=username)
        session.add(user)

    # def set_name(self, username):
    #     self.username = username
    #     user = User(username=self.username)
    #     session.add(user)




reg = Registration("VLAD")

qwe = {'name': 'GOVNOVOZ', 'number': '333', 'color': 'white'}

reg.add_car(**qwe)


# car = Car(name='KARETA', number='333', color='white')
# car1 = Car(name='bmw', number='111', color='white')

# user = User(username='daun')
# user = session.query(User).filter_by(username='adun').first()

# Establish relationship between the models
# user.cars.append(car)

# Add instances to the session and commit changes
# session.add(car)
# session.add(user)
# session.commit()

# user = session.query(User).filter_by(username='adun').first()

# cars = user.cars
# for car in cars:
#     print(car.name, car.number, car.color, car.user_id)

# Закрытие сеанса


session.commit()
session.close()
