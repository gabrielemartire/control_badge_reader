from sqlalchemy import create_engine # Import the SQLAlchemy create_engine function to create a database engine.
from sqlalchemy.orm import Session
from models.base import Base
from cli.role_cli import role_submenu
from cli.user_cli import user_submenu
from cli.badge_cli import badge_submenu
from cli.badge_reader_cli import badge_reader_submenu
from cli.access_cli import access_submenu
from cli.relations_cli import relation_submenu
from cli.sector_cli import sector_submenu
from cli.warning_cli import warning_submenu
from db.use_seeds import use_seeds


engine = create_engine("mysql+pymysql://root:Password123!@127.0.0.1/db") # Create a MySQL database engine (://username:pwd@host/db_name)
session = Session(bind=engine) # Create a session, to handle database
Base.metadata.create_all(bind=engine) # Create the database tables defined in the Base class

print("""
    CONTROL BADGE RE▲DER SYSTEM
    Gabriele Martire
    Matr.: IN09000637
""")

while True:
    print("-" *10 + "Models Menu" + "-" *10)
    print("1 - ROLES")
    print("2 - USERS")
    print("3 - BADGES")
    print("4 - BADGES_READER")
    print("5 - ACCESS")
    print("6 - SECTOR")
    print("7 - WARNING")
    print("8 - RELATIONS")
    print("9 - SEEDs")
    print("0 - EXIT")

    model_selected = int(input("select model: "))

    match model_selected:
        case 0: break
        case 1: role_submenu(session)
        case 2: user_submenu(session)
        case 3: badge_submenu(session)
        case 4: badge_reader_submenu(session)
        case 5: access_submenu(session)
        case 6: sector_submenu(session)
        case 7: warning_submenu(session)
        case 8: relation_submenu(session)
        case 9: use_seeds(session)
        case _: print("invalid choice")


