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
    """
    The ProjectUserService class is a utility 
    class that provides a static method for adding a 
    ProjectUserService object to the database.

    Attributes
    -------
    None
    
    Methods
    -------
    add(project_id: int, user_id: int) -> None: 
    creates a new ProjectUserService object using the provided project_id 
    and user_id, adds it to the current session and commits the transaction. 
    The method returns nothing (None).
    This class assumes that a valid ProjectUserService object is provided to the session, 
    with valid project_id and user_id values. It's up to the caller to ensure that 
    these values are valid before calling this method.
    """
    @staticmethod
    def add(project_id: int, user_id: int)->None:
        project_user = ProjectUser(project_id=project_id, user_id=user_id)
        session.add(project_user)
        session.commit()