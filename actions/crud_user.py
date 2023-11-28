from datetime import datetime
from models.user import User
from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session

def create_user(session: Session, user_info: dict):
    session.add(User(**user_info))
    session.commit()
    return user_info

def retrieve_user(session: Session, user_id: int):
    sql_statement = select(User).where(User.id== user_id)
    user = session.scalars(sql_statement).one_or_none()
    return user.__dict__ if user is not None else None

def update_user(session: Session, user_id: int, user_info: dict):
    user_info["updated_at"] = datetime.now()
    sql_statement = update(User).where(User.id== user_id).values(**user_info)
    session.execute(sql_statement)
    session.commit()
    sql_statement = select(User).where(User.id== user_id)
    user_updated = session.scalars(sql_statement).one_or_none()
    return user_updated.__dict__ if user_updated is not None else None

def delete_user(session: Session, user_id: int):
    sql_statement = update(User).where(User.id== user_id).values({"deleted_at": datetime.now()})
    session.execute(sql_statement)
    session.commit()
    return user_id