from datetime import datetime
from models.warning import Warning
from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session

def create_warning(session: Session, warning_info: dict): #todo
    session.add(Warning(**warning_info))
    session.commit()
    return warning_info

def retrieve_warning(session: Session, warning_id: int): #todo
    sql_statement = select(Warning).where(Warning.id== warning_id)
    warning = session.scalars(sql_statement).one_or_none()
    return warning.__dict__ if warning is not None else None

def update_warning(session: Session, warning_id: int, warning_info: dict): #todo
    warning_info["updated_at"] = datetime.now()
    sql_statement = update(Warning).where(Warning.id== warning_id).values(**warning_info)
    session.execute(sql_statement)
    session.commit()
    sql_statement = select(Warning).where(Warning.id== warning_id)
    warning_updated = session.scalars(sql_statement).one_or_none()
    return warning_updated.__dict__ if warning_updated is not None else None

def delete_warning(session: Session, warning_id: int):
    sql_statement = update(Warning).where(Warning.id== warning_id).values({"deleted_at": datetime.now()})
    session.execute(sql_statement)
    session.commit()
    return warning_id