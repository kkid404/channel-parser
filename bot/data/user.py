from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from data.data import session, Base, SessionLocal

db = SessionLocal()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(125))
    chat_id = Column(String(125), unique=True)

    channels = relationship("ChannelUser", back_populates="user")

class UserService:

    @staticmethod
    def add(name, chat_id):
        user = User(name=str(name), chat_id=str(chat_id))
        session.add(user)
        session.commit()
        return user.id

    @staticmethod
    def get(chat_id):
        user =  session.query(User).filter(User.chat_id == str(chat_id)).first()
        if user:
            return user.id

