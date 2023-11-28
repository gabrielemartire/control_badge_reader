
from actions.crud_badge_reader_role import create_badge_reader_role
from actions.crud_badge_reader_warning import create_badge_reader_warning
#from db.seed import BADGE_READERS_ROLES, BADGE_READERS_WARNINGS

def relation_submenu(session):
    while True:
        print("available actions:")
        print("1 - create new badge_reader-role relation")
        print("2 - create new badge_reader-warning relation")
        print("0 - back")

        crud_selected = input("select action: ")

        if crud_selected == "1":
            badge_reader_id = input("insert badge reader id: ")
            role_id = int(input("insert role id: "))
            badge_reader_role_info = {"badge_reader_id": badge_reader_id, "role_id": role_id}
            print(create_badge_reader_role(session=session, badge_reader_role_info=badge_reader_role_info))

        elif crud_selected == "2":
            warning_id = input("insert warning id: ")
            badge_reader_id = int(input("insert  badge reader id: "))
            badge_reader_warning_info = {"warning_id": warning_id, "badge_reader_id": badge_reader_id}
            print(create_badge_reader_warning(session=session, badge_reader_warning_info=badge_reader_warning_info))

        elif crud_selected == "0":
            break
        else:
            print("ERROR")
