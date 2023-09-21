import mysql.connector

import sqlalchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:abc123@localhost:3306/dbspecjalna',echo=True)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(length=50))
    fullname = sqlalchemy.Column(sqlalchemy.String(length=50))
    nickname = sqlalchemy.Column(sqlalchemy.String(length=50))

    def __repr__(self):
        return f"<User -> name: {self.name}, full name: {self.fullname}, nick name: {self.nickname}>"

Base.metadata.create_all(engine)

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

us1 = User(name = 'Marcin', fullname = 'Marcin Albiniak', nickname = 'viking')
session.add(us1)

us2 = User(name = 'Ewa', fullname = 'Ewa Kot', nickname = 'ewcia')
session.add(us2)

us3 = User(name = 'Olaf', fullname = 'Olaf Kos', nickname = 'olo')
session.add(us3)

session.commit()
print("_"*35)

for s in session.query(User).all():
    print(s)

print("_"*35)

for s in session.query(User).filter(User.nickname=='olo'):
    print(s.fullname)





