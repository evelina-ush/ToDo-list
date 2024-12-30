from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base


engine = create_engine("sqlite:///./tasks.db")

Session = sessionmaker(autocommit=False, autoflush=True, bind=engine)

Base.metadata.create_all(engine)