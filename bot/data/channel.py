from typing import Union

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from data.data import session, Base, SessionLocal

db = SessionLocal()

class Channel(Base):
    __tablename__ = 'channels'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), default=None)
    link = Column(String(250), unique=True)
    channel_id = Column(String(250), default=None)

    users = relationship("ChannelUser", back_populates="channel")

class ChannelService:
    """
    This ChannelService class contains two static methods 
    to work with the Channel model using the SQLAlchemy ORM library.
    """
    @staticmethod
    def add(link: str)->int:
        """
        The add method takes a reference to a channel, creates a new instance of the 
        Channel class with the passed reference, adds it to the database, and commits changes 
        using session.commit().

        Returns
        -------
        int
            Created class ID.
        """
        channel = Channel(link=link)
        session.add(channel)
        session.commit()
        return channel.id

    @staticmethod
    def get_link(link: str) -> Union[int, None]:
        """
        The get_link method takes a reference to a channel and uses the filter 
        method of db.query(Channel) object to search for the channel by the passed reference. 

        Returns
        -------
        int
            If the channel is found, the method returns its identifier. 
        None
            If the channel is not found
        """
        channel = session.query(Channel).filter(Channel.link == link).first()
        if channel:
            return channel.id

