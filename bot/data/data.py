from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


from loader import USERNAME, PASSWORD, HOST, PORT, DATABASE

engine = create_engine(f'mysql+mysqlconnector://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

