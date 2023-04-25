from typing import Union

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from data.data import session, Base, SessionLocal
from data.project_user import ProjectUser


db = SessionLocal()

class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(125))
    chat_id = Column(String(125), unique=True)

    channels = relationship("ChannelUser", back_populates="user")
    projects = relationship("ProjectUser", back_populates="user")

class UserService:
    """
    This UserService class contains two static methods 
    to work with the User model using the SQLAlchemy ORM library.
    """
    @staticmethod
    def add(name: str, chat_id: int)->int:
        """
        The add method takes a reference to a channel, creates a new instance of the 
        Channel class with the passed reference, adds it to the database, and commits changes 
        using session.commit().

        Returns
        -------
        int
            Created class ID.
        """
        user = User(name=str(name), chat_id=str(chat_id))
        session.add(user)
        session.commit()
        return user.id

    @staticmethod
    def get(chat_id: int)->Union[int, None]:
        """
        The get method takes a reference to a user and uses the filter 
        method of db.query(User) object to search for the user by the passed reference. 

        Returns
        -------
        int
            If the user is found, the method returns its identifier. 
        None
            If the user is not found
        """
        user =  session.query(User).filter(User.chat_id == str(chat_id)).first()
        if user:
            return user.id

