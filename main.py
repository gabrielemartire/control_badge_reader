from sqlalchemy import create_engine
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
from db.use_seed import use_seed


engine = create_engine("mysql+pymysql://root:Password123!@127.0.0.1/db")
session = Session(bind=engine)
Base.metadata.create_all(bind=engine) #Crea tutte le tabelle dei modelli che hanno ereditato Base

print("""
    CONTROL BADGE RE▲DER SYSTEM
    Gabriele Martire
    Matr.: IN09000637
""")

while True:
    # Stampa il menu
    print("-" *10 + "Models Menu" + "-" *10)
    print("1 - ROLES")
    print("2 - USERS")
    print("3 - BADGES")
    print("4 - BADGES_READER")
    print("5 - ACCESS")
    print("6 - SECTOR")
    print("7 - WARNING")
    print("8 - RELATIONS")
    print("9 - SEED")
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
        case 9: use_seed(session)
        case _: print("value not valid")


