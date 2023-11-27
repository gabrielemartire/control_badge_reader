from datetime import datetime
from models.role import Role
from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session

def create_role(session: Session, role_info: dict):
    session.add(Role(**role_info))
    session.commit()

def retrieve_role(session: Session, id: int):
    sql_statement = select(Role).where(Role.id== id)
    role = session.scalars(sql_statement).one_or_none()
    return role.__dict__

def update_role(session: Session, id: int, role_info: dict):
    role_info["updated_at"] = datetime.now()
    sql_statement = update(Role).where(Role.id== id).values(**role_info)
    session.execute(sql_statement)
    session.commit()
    sql_statement = select(Role).where(Role.id== id)
    role_updated = session.scalars(sql_statement).one_or_none()
    return role_updated.__dict__

def delete_role(session: Session, id: int):
    sql_statement = delete(Role).where(Role.id== id)
    session.execute(sql_statement)
    session.commit()
    return id
