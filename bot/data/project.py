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
    """
    This ProjectService class contains two static methods 
    to work with the Channel model using the SQLAlchemy ORM library.
    """
    @staticmethod
    def add(name: str)->int:
        """
        The add method takes a reference to a project, creates a new instance of the 
        Project class with the passed reference, adds it to the database, and commits changes 
        using session.commit().

        Returns
        -------
        int
            Created class ID.
        """
        project = Project(name=name)
        session.add(project)
        session.commit()
        return project.id

    @staticmethod
    def get_id(name)->int:
        """
        The get_id method takes a reference to a project and uses the filter 
        method of db.query(Project) object to search for the project by the passed reference. 

        Returns
        -------
        int
            If the project is found, the method returns its identifier. 
        None
            If the project is not found
        """
        project =  session.query(Project).filter(Project.name == name).first()
        if project:
            return project.id
