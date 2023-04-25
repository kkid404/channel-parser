from sqlalchemy import Column, Integer, String

from data.data import session, Base, SessionLocal
from sqlalchemy.orm import relationship

db = SessionLocal()

class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), default=None)

    users = relationship("ProjectUser", back_populates="project")

class ProjectService:

    @staticmethod
    def add(name):
        project = Project(name=name)
        session.add(project)
        session.commit()
        return project.id

    @staticmethod
    def get_id(name):
        project =  db.query(Project).filter(name == name).first()
        if project:
            return project.id
        else:
            None