from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from data.data import session, Base, SessionLocal

class ProjectUser(Base):

    __tablename__ = "projects_users"

    project_id = Column(Integer, ForeignKey("projects.id"), primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    
    project = relationship("Project", back_populates="users")
    user = relationship("User", back_populates="projects")

class ProjectUserService:
    
    @staticmethod
    def add(project_id: int, user_id: int)->None:
        project_user = ProjectUser(project_id=project_id, user_id=user_id)
        session.add(project_user)
        session.commit()