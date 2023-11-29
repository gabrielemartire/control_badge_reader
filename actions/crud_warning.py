from datetime import datetime
from models.warning import Warning
from sqlalchemy import select, update
from models.base import badge_readers_warnings
from sqlalchemy.orm import Session

def create_warning(session: Session, warning_info: dict):
    session.add(Warning(**warning_info))
    session.commit()
    return warning_info

def retrieve_warning(session: Session, warning_id: int):
    sql_statement = select(Warning).where(Warning.id== warning_id)
    warning = session.scalars(sql_statement).one_or_none()
    return warning.__dict__ if warning is not None else None

def update_warning(session: Session, warning_id: int, warning_info: dict):
    warning_info["updated_at"] = datetime.now()
    sql_statement = update(Warning).where(Warning.id== warning_id).values(**warning_info)
    session.execute(sql_statement)
    session.commit()
    sql_statement = select(Warning).where(Warning.id== warning_id)
    warning_updated = session.scalars(sql_statement).one_or_none()
    return warning_updated.__dict__ if warning_updated is not None else None

# soft seltes warning
def delete_warning(session: Session, warning_id: int):
    warning = session.query(Warning).get(warning_id)

    # we cannot proceed with the delete cascade cause we are using an association table without a dedicated BadgeReaderRole model
    # in this case it is not possible to use delete-orphan for many-to-many relationships
    # so we proceed by first deleting the records in the join table and then soft delete the specific warning
    if warning:
        session.execute(badge_readers_warnings.delete().where(badge_readers_warnings.c.warning_id == warning_id))
        warning.deleted_at = datetime.now()
        session.commit()

    return warning_id
