from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from data.data import session, Base, SessionLocal

class ChannelUser(Base):

    __tablename__ = "channels_users"

    channel_id = Column(Integer, ForeignKey("channels.id"), primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    
    channel = relationship("Channel", back_populates="users")
    user = relationship("User", back_populates="channels")

class ChannelUserService:
    """
    The ChannelUserService class is a utility 
    class that provides a static method for adding a 
    ChannelUser object to the database.

    Attributes
    -------
    None
    
    Methods
    -------
    add(channel_id: int, user_id: int) -> None: 
    creates a new ChannelUser object using the provided channel_id 
    and user_id, adds it to the current session and commits the transaction. 
    The method returns nothing (None).
    This class assumes that a valid ChannelUser object is provided to the session, 
    with valid channel_id and user_id values. It's up to the caller to ensure that 
    these values are valid before calling this method.
    """
    @staticmethod
    def add(channel_id: int, user_id: int)->None:
        channel_user = ChannelUser(channel_id=channel_id, user_id=user_id)
        session.add(channel_user)
        session.commit()