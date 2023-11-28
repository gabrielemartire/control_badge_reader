from datetime import datetime
from models.access import Access
from sqlalchemy import select, update, and_
from sqlalchemy.orm import Session
from models.badge import Badge 
from models.user import User
from models.role import Role
from models.badge_reader import BadgeReader

# when user get in
def create_access(session: Session, access_info: dict):

    badge_id = access_info.get('badge_id', None)
    badge_reader_id = access_info.get('badge_reader_id', None)

    if badge_id and badge_reader_id:

        access = Access(**access_info)

        sql_statement = select(Badge).where(Badge.id == badge_id)
        badge = session.scalars(sql_statement).one_or_none()

        sql_statement = select(Role).where(Role.id == badge.user.role_id)
        role = session.scalars(sql_statement).one_or_none()

        sql_statement = select(BadgeReader).where(BadgeReader.id == badge_reader_id)
        br = session.scalars(sql_statement).one_or_none()

        if role in br.roles:
            access.timestamp_in = datetime.now()

        session.add(access)
        session.commit()
        return True

    return False

def retrieve_access(session: Session, badge_id: int, badge_reader_id: int):
    sql_statement = select(Access).where(and_(Access.badge_id == badge_id, Access.badge_reader_id == badge_reader_id))
    access = session.scalars(sql_statement).one_or_none()
    return access.__dict__ if access is not None else None

# when user get out
def update_access(session: Session, badge_id: int, badge_reader_id: int, access_info: dict):
    access_info["timestamp_out"] = datetime.now()
    sql_statement = update(Access).where(and_(Access.badge_id == badge_id, Access.badge_reader_id == badge_reader_id)).values(**access_info)
    session.execute(sql_statement)
    session.commit()
    sql_statement = select(Access).where(and_(Access.badge_id == badge_id, Access.badge_reader_id == badge_reader_id))
    access_updated = session.scalars(sql_statement).one_or_none()
    return access_updated.__dict__ if access_updated is not None else None
