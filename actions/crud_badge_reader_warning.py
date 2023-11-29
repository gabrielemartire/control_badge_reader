from datetime import datetime
from models.base import badge_readers_warnings
from sqlalchemy.orm import Session

def create_badge_reader_warning(session: Session, badge_reader_warning_info: dict):
    session.execute(badge_readers_warnings.insert().values(badge_reader_warning_info))
    session.commit()
