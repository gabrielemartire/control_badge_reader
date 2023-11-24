from datetime import datetime
from models.warning import Warning
from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session

def create_warning(session: Session, warning_info: dict): #todo
    session.add(Warning(**warning_info))
    session.commit()

def retrive_warning(session: Session, id: int): #todo
    sql_statement = select(Warning).where(Warning.id== id)
    warning = session.scalars(sql_statement).one_or_none()
    return warning.__dict__

def update_warning(session: Session, id: int, warning_info: dict): #todo
    warning_info["updated_at"] = datetime.now()
    sql_statement = update(Warning).where(Warning.id== id).values(**warning_info)
    session.execute(sql_statement)
    session.commit()
    sql_statement = select(Warning).where(Warning.id== id)
    warning_updated = session.scalars(sql_statement).one_or_none()
    return warning_updated.__dict__

def delete_warning(session: Session, id: int): #todo
    sql_statement = delete(Warning).where(Warning.id== id)
    session.execute(sql_statement)
    session.commit()
    return id
