
from actions.crud_access import create_access, retrieve_access, update_access
from db.seed import ACCESSES

def access_submenu(session):
    while True:
        print("available actions:")
        print("1 - ENTER A SPECIFIC AREA WITH A SPECIFIC BADGE (create new access)")
        print("2 - SHOW ACCESS LOG (retrieve an access)")
        print("3 - EXIT A SPECIFIC AREA WITH A SPECIFIC BADGE (update an access)")
        print("0 - back")

        crud_selected = int(input("select action: "))

        match crud_selected:
            case 1:
                badge_id_selected = int(input("insert badge id: "))
                badge_reader_id_selected = int(input("insert badge reader id: "))
                new_access_dict = {"badge_id": badge_id_selected, "badge_reader_id": badge_reader_id_selected}
                scan_sts = create_access(session = session, access_info = new_access_dict)
                if scan_sts:
                    print("authorized")
                else:
                    print("not authorized")
            
            case 2:
                badge_id_selected = int(input("insert badge id: "))
                badge_reader_id_selected = int(input("insert badge reader id: "))
                print(retrieve_access(session = session, badge_id = badge_id_selected, badge_reader_id = badge_reader_id_selected))

            case 3:
                badge_id_selected = int(input("insert badge id: "))
                badge_reader_id_selected = int(input("insert badge reader id: "))
                print(update_access(session = session, badge_id = badge_id_selected, badge_reader_id = badge_reader_id_selected))

            case 0: break

            case _: print("ERROR")

