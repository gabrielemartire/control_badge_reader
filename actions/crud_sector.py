from datetime import datetime
from models.sector import Sector
from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session

def create_sector(session: Session, sector_info: dict):
    session.add(Sector(**sector_info))
    session.commit()
    return sector_info

def retrieve_sector(session: Session, sector_id: int):
    sql_statement = select(Sector).where(Sector.id== sector_id)
    sector = session.scalars(sql_statement).one_or_none()
    return sector.__dict__ if sector is not None else None

def update_sector(session: Session, sector_id: int, sector_info: dict):
    sector_info["updated_at"] = datetime.now()
    sql_statement = update(Sector).where(Sector.id== sector_id).values(**sector_info)
    session.execute(sql_statement)
    session.commit()
    sql_statement = select(Sector).where(Sector.id== sector_id)
    sector_updated = session.scalars(sql_statement).one_or_none()
    return sector_updated.__dict__ if sector_updated is not None else None

def delete_sector(session: Session, sector_id: int):
    sql_statement = delete(Sector).where(Sector.id== sector_id)
    session.execute(sql_statement)
    session.commit()
    return sector_id
