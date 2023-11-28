from datetime import datetime
from models.badge_reader import BadgeReader
from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session

def create_badge_reader(session: Session, badge_reader_info: dict):
    session.add(BadgeReader(**badge_reader_info))
    session.commit()

def retrieve_badge_reader(session: Session, badge_reader_id: int):
    sql_statement = select(BadgeReader).where(BadgeReader.id== badge_reader_id)
    badge_reader = session.scalars(sql_statement).one_or_none()
    return badge_reader.__dict__ if badge_reader is not None else None

def update_badge_reader(session: Session, badge_reader_id: int, badge_reader_info: dict):
    badge_reader_info["updated_at"] = datetime.now()
    sql_statement = update(BadgeReader).where(BadgeReader.id== badge_reader_id).values(**badge_reader_info)
    session.execute(sql_statement)
    session.commit()
    sql_statement = select(BadgeReader).where(BadgeReader.id== badge_reader_id)
    badge_reader_updated = session.scalars(sql_statement).one_or_none()
    return badge_reader_updated.__dict__ if badge_reader_updated is not None else None

def delete_badge_reader(session: Session, badge_reader_id: int):
    sql_statement = delete(BadgeReader).where(BadgeReader.id== badge_reader_id)
    session.execute(sql_statement)
    session.commit()
    return id