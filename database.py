from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date

Base = declarative_base()


class Tasks(Base):
    __tablename__ = "tasks"

    id = Column("ID", Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column("Name", String, nullable=False)
    description = Column("Description", String, nullable=False)
    deadline = Column("Deadline", Date, nullable=False)

    def __init__(self, name, descriprion, deadline):
        self.name = name
        self.description = descriprion
        self.deadline = deadline

