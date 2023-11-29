from datetime import datetime, timedelta
from models.badge_reader import BadgeReader
from models.base import badge_readers_roles
from models.base import badge_readers_warnings
from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session

def create_badge_reader(session: Session, badge_reader_info: dict):
    session.add(BadgeReader(**badge_reader_info))
    session.commit()
    return badge_reader_info

def retrieve_badge_reader(session: Session, badge_reader_id: int):
    sql_statement = select(BadgeReader).where(BadgeReader.id== badge_reader_id)
    badge_reader = session.scalars(sql_statement).one_or_none()
    return badge_reader.__dict__ if badge_reader is not None else None

def update_badge_reader(session: Session, badge_reader_id: int, badge_reader_info: dict):
    badge_reader_info["updated_at"] = datetime.now()
    badge_reader_info["maintenance_at"] =(datetime.now() + timedelta(days=365 * 2))
    sql_statement = update(BadgeReader).where(BadgeReader.id== badge_reader_id).values(**badge_reader_info)
    session.execute(sql_statement)
    session.commit()
    sql_statement = select(BadgeReader).where(BadgeReader.id== badge_reader_id)
    badge_reader_updated = session.scalars(sql_statement).one_or_none()
    return badge_reader_updated.__dict__ if badge_reader_updated is not None else None

def delete_badge_reader(session: Session, badge_reader_id: int):
    badge_reader = session.query(BadgeReader).get(badge_reader_id)

    # we cannot proceed with the delete cascade cause we are using an association table without a dedicated BadgeReaderRole model
    # in this case it is not possible to use delete-orphan for many-to-many relationships
    # so we proceed by first deleting the records in the join table and then the specific badge_reader
    if badge_reader:
        session.execute(badge_readers_roles.delete().where(badge_readers_roles.c.badge_reader_id == badge_reader_id))
        session.execute(badge_readers_warnings.delete().where(badge_readers_warnings.c.badge_reader_id == badge_reader_id))
        session.execute(delete(badge_reader))
        session.commit()

    return badge_reader_id