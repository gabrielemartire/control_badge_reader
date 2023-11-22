from datetime import datetime
from models.badge import Badge
from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session

def create_badge(session: Session, badge_info: dict):
    session.add(Badge(**badge_info))
    session.commit()

def retrive_badge(session: Session, id: int):
    sql_statement = select(Badge).where(Badge.id== id)
    badge = session.scalars(sql_statement).one()
    badge.__dict__["user"] = badge.user.full_name
    return badge.__dict__

def update_badge(session: Session, id: int, badge_info: dict):
    badge_info["updated_at"] = datetime.now()
    sql_statement = update(Badge).where(Badge.id== id).values(**badge_info)
    session.execute(sql_statement)
    session.commit()
    sql_statement = select(Badge).where(Badge.id== id)
    badge_updated = session.scalars(sql_statement).one()
    return badge_updated.__dict__

def delete_badge(session: Session, id: int):
    sql_statement = delete(Badge).where(Badge.id== id)
    session.execute(sql_statement)
    session.commit()
    return id

