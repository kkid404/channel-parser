from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from data.data import session, Base, SessionLocal

class ChannelUser(Base):

    __tablename__ = "channels_users"

    channel_id = Column(Integer, ForeignKey("channels.id"), primary_key=True)
    user_ud = Column(Integer, ForeignKey("users.id"), primary_key=True)
    
    channel = relationship("Channel", back_populates="users")
    user = relationship("User", back_populates="channels")

class ChannelUserService:
    
    @staticmethod
    def add(channel_id: int, user_id: int)->None:
        channel_user = ChannelUser(channel_id=channel_id, user_id=user_id)
        session.add(channel_user)
        session.commit()