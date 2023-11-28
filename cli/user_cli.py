
from actions.crud_user import create_user, retrieve_user, update_user, delete_user
#from db.seed import USERS

def user_submenu(session):
    while True:
        print("available actions:")
        print("1 - create new user")
        print("2 - retrieve user")
        print("3 - update user")
        print("4 - delete user")
        print("0 - back")

        crud_selected = input("select action: ")

        if crud_selected == "1":
            full_name_selected = input("insert user full name: ")
            role_id_selected = input("insert insert role id: ")
            new_role_dict = {"full_name": full_name_selected, "role_id": role_id_selected}
            print(create_user(session = session, user_info = new_role_dict))

        elif crud_selected == "2":
            user_id = input("insert user id: ")
            print(retrieve_user(session = session, user_id = user_id))

        elif crud_selected == "3":
            user_id = input("insert user user id: ")
            full_name_selected = input("insert user full name: ")
            role_id_selected = input("insert role id: ")
            upd_user_dict = {"full_name": full_name_selected, "role_id": role_id_selected}
            print(update_user(session = session, user_id = user_id, user_info = upd_user_dict))

        elif crud_selected == "4":
            user_id = input("insert user id: ")
            print(delete_user(session = session, user_id = user_id))

        elif crud_selected == "0":
            break
        else:
            print("ERROR")
