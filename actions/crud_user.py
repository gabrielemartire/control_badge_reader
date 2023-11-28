from datetime import datetime
from models.user import User
from sqlalchemy import select, update
from sqlalchemy.orm import Session

def create_user(session: Session, user_info: dict):
    # Args: session is from SQLAlchemy and user_info is a dictionary with user information
    session.add(User(**user_info))
    session.commit()
    return user_info

def retrieve_user(session: Session, user_id: int):
    # Args: user_id is the user's id to find
    sql_statement = select(User).where(User.id== user_id)
    user = session.scalars(sql_statement).one_or_none()
    return user.__dict__ if user is not None else None
    # retrieve_user() return user's dictionary if user is not None
    # otherwise, return None to prevent exceptions

def update_user(session: Session, user_id: int, user_info: dict):
    #Args: user_id=ID user to update, user_info= dictionary containing new user information.
    user_info["updated_at"] = datetime.now()
    sql_statement = update(User).where(User.id== user_id).values(**user_info)
    session.execute(sql_statement)
    session.commit()
    sql_statement = select(User).where(User.id== user_id)
    user_updated = session.scalars(sql_statement).one_or_none()
    return user_updated.__dict__ if user_updated is not None else None
    # update_user() return user_update's dictionary if user is not None
    # otherwise, return None to prevent exceptions

# Soft deletes user by updating the 'deleted_at'.
def delete_user(session: Session, user_id: int):
    sql_statement = update(User).where(User.id== user_id).values({"deleted_at": datetime.now()})
    #Args: user_id=ID user to soft delete.
    session.execute(sql_statement)
    session.commit()
    return user_id