from models.base import badge_readers_roles
from sqlalchemy.orm import Session

def create_badge_reader_role(session: Session, badge_reader_role_info: dict):
    session.execute(badge_readers_roles.insert().values(badge_reader_role_info))
    session.commit()
