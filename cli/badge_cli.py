
from actions.crud_badge import create_badge, retrieve_badge, update_badge, delete_badge
#from db.seed import BADGES

def badge_submenu(session):
    while True:
        print("available actions:")
        print("1 - create new badge")
        print("2 - retrieve badge")
        print("3 - update badge")
        print("4 - delete badge")
        print("0 - BACK")

        crud_selected = input("select action: ")

        if crud_selected == "1":
            user_id_selected = input("insert user id: ")
            new_badge_dict = {"user_id": user_id_selected}
            print(create_badge(session = session, badge_info = new_badge_dict))

        elif crud_selected == "2":
            badge_id = input("insert id badge: ")
            print(retrieve_badge(session = session, badge_id = badge_id))

        elif crud_selected == "3":
            badge_id = input("badge badge id: ")
            user_id_selected = input("insert user id: ")
            upd_badge_dict = {"user_id": user_id_selected}
            print(update_badge(session = session, badge_id = badge_id, badge_info = upd_badge_dict))

        elif crud_selected == "4":
            badge_id = input("insert id badge: ")
            print(delete_badge(session = session, badge_id = badge_id))

        elif crud_selected == "0":
            break
        else:
            print("ERROR")
