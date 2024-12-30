from database import Tasks
from config import Session


def add_task(db: Session, name, description, deadline):
    this_task = Tasks(name, description, deadline)
    db.add(this_task)
    db.commit()
    db.refresh(this_task)


def delete_tea(db: Session, the_name):
    this_task = db.query(Tasks).filter(Tasks.name == the_name).first()
    db.delete(this_task)
    db.commit()
