
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

        crud_selected = input("select action: ")

        if crud_selected == "1":
            label_selected = input("insert role label: ")
            night_availability_selected = bool(input("is a night_availability role? (1/0): "))
            new_role_dict = {"label": label_selected, "night_availability_selected": night_availability_selected}
            print(create_role(session=session, role_info=new_role_dict))

        elif crud_selected == "2":
            role_id = input("insert role id: ")
            print(retrieve_role(session = session, role_id = role_id))

        elif crud_selected == "3":
            role_id = input("insert role id: ")
            label_selected = input("insert role label: ")
            night_availability_selected = bool(input("is a night_availability role? (1/0): "))
            upd_role_dict = {"label_selected": label_selected, "night_availability_selected": night_availability_selected}
            print(update_role(session = session, role_id = role_id, role_info=upd_role_dict))

        elif crud_selected == "4":
            role_id = input("insert role id: ")
            print(delete_role(session = session, role_id = role_id))
        elif crud_selected == "0":
            print("BACK")
            break
        else:
            print("ERROR")
