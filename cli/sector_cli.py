
from actions.crud_sector import create_sector, retrieve_sector, update_sector, delete_sector
#from db.seed import SECTORS

def sector_submenu(session):
    while True:
        print("available actions:")
        print("1 - create new sector")
        print("2 - retrieve sector")
        print("3 - update sector")
        print("4 - delete sector")
        print("0 - back")

        crud_selected = int(input("select action: "))

        match crud_selected:
            case 1:
                label_selected = input("insert sector label: ")
                role_id_selected = int(input("insert role id: "))
                under_uta_control_input = input("is an under_uta_control sector? (1/0): ") 
                under_uta_control_selected = True if under_uta_control_input == '1' else False
                new_sector_dict = {"label": label_selected, "role_id": role_id_selected, "under_uta_control": under_uta_control_selected}
                print(create_sector(session=session, sector_info=new_sector_dict))

            case 2:
                sector_id = int(input("insert sector id: "))
                print(retrieve_sector(session = session, sector_id = sector_id))

            case 3:
                sector_id = int(input("insert sector id: "))
                label_selected = input("insert sector label: ")
                role_id_selected = int(input("insert role id: "))
                under_uta_control_input = input("is an under_uta_control sector? (1/0): ") 
                under_uta_control_selected = True if under_uta_control_input == '1' else False
                upd_sector_dict = {"label": label_selected, "role_id": role_id_selected, "under_uta_control": under_uta_control_selected}
                print(update_sector(session = session, sector_id = sector_id, sector_info=upd_sector_dict))

            case 4:
                sector_id = int(input("insert sector id: "))
                print(delete_sector(session = session, sector_id = sector_id))

            case 0: break

            case _: print("ERROR")
