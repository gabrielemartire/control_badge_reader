
from actions.crud_role import create_role, retrieve_role, update_role, delete_role
#from db.seed import ROLES

def role_submenu(session):
    while True:
        print("available actions:")
        print("1 - create new role")
        print("2 - retrieve role")
        print("3 - update role")
        print("4 - delete role")
        print("0 - back")

        crud_selected = int(input("select action: "))

        match crud_selected:
            case 1:
                label_selected = input("insert role label: ")
                night_availability_input = input("is a night_availability role? (1/0): ") 
                night_availability_selected = True if night_availability_input == '1' else False
                new_role_dict = {"label": label_selected, "night_availability": bool(night_availability_selected)}
                print(create_role(session=session, role_info=new_role_dict))

            case 2:
                role_id = int(input("insert role id: "))
                print(retrieve_role(session = session, role_id = role_id))

            case 3:
                role_id = int(input("insert role id: "))
                label_selected = input("insert role label: ")
                night_availability_input = input("is a night_availability role? (1/0): ") 
                night_availability_selected = True if night_availability_input == '1' else False
                upd_role_dict = {"label": label_selected, "night_availability": night_availability_selected}
                print(update_role(session = session, role_id = role_id, role_info=upd_role_dict))

            case 4:
                role_id = int(input("insert role id: "))
                print(delete_role(session = session, role_id = role_id))

            case 0: break

            case _: print("ERROR")
