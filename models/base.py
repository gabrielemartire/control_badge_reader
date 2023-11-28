from sqlalchemy import Table, Column, ForeignKey, Integer
from sqlalchemy.orm import DeclarativeBase # it gives us access to the base declaration for the models we create

#Base(DeclarativeBase) to make Base inherit DeclarativeBase methods
class Base(DeclarativeBase):
    pass

badge_readers_roles = Table('badge_readers_roles', Base.metadata,
                            Column('badge_reader_id', Integer, ForeignKey('badge_readers.id')),
                            Column('role_id', Integer, ForeignKey('roles.id'))
                            )

badge_readers_warnings = Table('badge_readers_warnings', Base.metadata,
                            Column('badge_reader_id', Integer, ForeignKey('badge_readers.id')),
                            Column('warning_id', Integer, ForeignKey('warnings.id'))
                            )
