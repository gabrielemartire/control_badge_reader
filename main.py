from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session # classe
from actions.crud_user import create_user, retrive_user, update_user, delete_user
from actions.crud_badge import create_badge, retrive_badge, update_badge, delete_badge
from actions.crud_badge_reader import create_badge_reader, retrive_badge_reader, update_badge_reader, delete_badge_reader
from actions.crud_sector import create_sector, retrive_sector, update_sector, delete_sector
from actions.crud_role import create_role, retrive_role, update_role, delete_role
from actions.crud_access import create_access, retrive_access, update_access
from actions.crud_badge_reader_role import create_badge_reader_role
from db.seed import USERS, BADGES, ROLES, SECTORS, BADGE_READERS, WARNINGS, BADGE_READERS_ROLES, ACCESSES
from models.base import Base
from datetime import datetime
from models.user import User
from models.badge import Badge
from models.role import Role
from models.sector import Sector
from models.badge_reader import BadgeReader
from models.access import Access

engine = create_engine("mysql+pymysql://root:Password123!@127.0.0.1/db")
session = Session(bind=engine)
Base.metadata.create_all(bind=engine) #Crea tutte le tabelle dei modelli che hanno ereditato Base

## CRUD role
for r in ROLES:
    create_role(session=session, role_info = r)
##print(retrive_role(session=session, id=1))
##update_role(session=session, id=1, role_info={"night_availability": True})
##delete_role(session=session, id=2)
#
## CRUD user
#for u in USERS:
#    create_user(session=session, user_info= u)
#print(retrive_user(session=session, id=1))
#update_user(session=session, id=1, user_info={"full_name": "Jesse Faden"})
#delete_user(session=session, id=3)

# CRUD badge
#for b in BADGES:
#    create_badge(session=session, badge_info= b)
#print(retrive_badge(session=session, id=1))
#update_badge(session=session, id=1, badge_info={"user_id": "2"})
#delete_badge(session=session, id=2)

# CRUD sector
#for s in SECTORS:
#    create_sector(session=session, sector_info= s)

# CRUD badge reader
#for br in BADGE_READERS:
#    create_badge_reader(session=session, badge_reader_info= br)
#print(retrive_badge(session=session, id=1))
#update_badge(session=session, id=1, data_info={"user_id": "2"})
#delete_badge(session=session, id=2)

# CRUD badge_readers_roles
#for rbr in BADGE_READERS_ROLES:
#    create_badge_reader_role(session=session, role_badge_reader_info= rbr)

# CRUD accesses
#for a in ACCESSES:
#    create_access(session=session, access_info=a)

#print(retrive_badge(session=session, id=1))
#update_badge(session=session, id=1, data_info={"user_id": "2"})
#delete_badge(session=session, id=2)

