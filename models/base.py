from sqlalchemy import Table, Column, ForeignKey, Integer
from sqlalchemy.orm import DeclarativeBase # ci da accesso alla dichiarazione base per i modelli che creiamo

#Base(DeclarativeBase) per far ereditare a Base i metodi di DeclarativeBase
class Base(DeclarativeBase):
    pass

badge_readers_roles = Table('badge_readers_roles', Base.metadata,
                            Column('badge_reader_id', Integer, ForeignKey('badge_readers.id')),
                            Column('role_id', Integer, ForeignKey('roles.id'))
                            )
