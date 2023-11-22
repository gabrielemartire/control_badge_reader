from datetime import datetime
from models.access import Access
from sqlalchemy import select, update
from sqlalchemy.orm import Session

# when user get in
def create_access(session: Session, access_info: dict):
    session.add(Access(**access_info))
    session.commit()

def retrive_access(session: Session, id: int):
    sql_statement = select(Access).where(Access.id == id)
    access = session.scalars(sql_statement).one()
    return access.__dict__

# when user get out
def update_access(session: Session, badge_id: int, badge_reader_id: int, access_info: dict):
    access_info["timestamp_out"] = datetime.now()
    sql_statement = update(Access).where(Access.badge_id == badge_id).where(Access.badge_reader_id == badge_reader_id).values(**access_info)
    session.execute(sql_statement)
    session.commit()
    sql_statement = select(Access).where(Access.badge_id == badge_id).where(Access.badge_reader_id == badge_reader_id)
    access_updated = session.scalars(sql_statement).one()
    return access_updated.__dict__
