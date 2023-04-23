from sqlalchemy import Column, Integer, String

from data.data import session, Base, SessionLocal

db = SessionLocal()

class Channel(Base):
    __tablename__ = 'channels'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), default=None)
    link = Column(String(250), unique=True)
    channel_id = Column(String(250), default=None)

class ChannelService:

    @staticmethod
    def add(link):
        channel = Channel(link=link)
        session.add(channel)
        session.commit()

    @staticmethod
    def get_link(link):
        channel = db.query(Channel).filter_by(link=link).first()
        if channel:
            return channel
        else:
            False