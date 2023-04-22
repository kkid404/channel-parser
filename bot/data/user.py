from sqlalchemy import Column, Integer, String

from data.data import session, Base, SessionLocal

db = SessionLocal()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(125))
    chat_id = Column(String(125), unique=True)

class UserService:

    @staticmethod
    def add(name, chat_id):
        user = User(name=name, chat_id=chat_id)
        session.add(user)
        session.commit()

    @staticmethod
    def get(chat_id):
        user = db.query(User).filter_by(chat_id=chat_id).first()
        if user:
            return user
        else:
            False
