from datetime import datetime
from models.sector import Sector
from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session

def create_sector(session: Session, sector_info: dict):
    session.add(Sector(**sector_info))
    session.commit()

def retrive_sector(session: Session, id: int):
    sql_statement = select(Sector).where(Sector.id== id)
    sector = session.scalars(sql_statement).one()
    return sector.__dict__

def update_sector(session: Session, id: int, sector_info: dict):
    sector_info["updated_at"] = datetime.now()
    sql_statement = update(Sector).where(Sector.id== id).values(**sector_info)
    session.execute(sql_statement)
    session.commit()
    sql_statement = select(Sector).where(Sector.id== id)
    sector_updated = session.scalars(sql_statement).one()
    return sector_updated.__dict__

def delete_sector(session: Session, id: int):
    sql_statement = delete(Sector).where(Sector.id== id)
    session.execute(sql_statement)
    session.commit()
    return id
