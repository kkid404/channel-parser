from sqlalchemy import Column, Integer, String

from data.data import session, Base, SessionLocal

db = SessionLocal()

class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), default=None)

class ProjectService:

    @staticmethod
    def add(name):
        channel = Project(name=name)
        session.add(channel)
        session.commit()

    @staticmethod
    def get_name(name):
        channel = db.query(Project).filter_by(name=name).first()
        if channel:
            return channel
        else:
            False