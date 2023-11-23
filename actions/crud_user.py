from datetime import datetime
from models.user import User
from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session

def create_user(session: Session, user_info: dict):
    session.add(User(**user_info))
    session.commit()

def retrive_user(session: Session, id: int):
    sql_statement = select(User).where(User.id== id)
    user = session.scalars(sql_statement).one_or_none()
    return user.__dict__

def update_user(session: Session, id: int, user_info: dict):
    user_info["updated_at"] = datetime.now()
    sql_statement = update(User).where(User.id== id).values(**user_info)
    session.execute(sql_statement)
    session.commit()
    sql_statement = select(User).where(User.id== id)
    user_updated = session.scalars(sql_statement).one_or_none()
    return user_updated.__dict__

#def delete_user(session: Session, id: int):
#    sql_statement = delete(User).where(User.id== id)
#    session.execute(sql_statement)
#    session.commit()
#    return id

def delete_user(session, user_id):
    user = session.query(User).get(user_id)
    print(user)
    print(session)
    if user:
        session.delete(user)
        session.commit()
        return user_id
    else:
        return None