
from actions.crud_badge_reader import create_badge_reader, retrieve_badge_reader, update_badge_reader, delete_badge_reader
#from db.seed import BADGE_READERS

def badge_reader_submenu(session):
    while True:
        print("available actions:")
        print("1 - create new badge reader")
        print("2 - retrieve badge reader")
        print("3 - update badge reader")
        print("4 - delete badge reader")
        print("0 - back")

        crud_selected = input("select action: ")

        if crud_selected == "1":
            label_selected = input("insert badge reader label: ")
            sector_id_selected = input("insert sector id: ")
            new_badge_reader_dict = {"label": label_selected, "sector_id": sector_id_selected}
            print(create_badge_reader(session = session, badge_reader_info = new_badge_reader_dict))

        elif crud_selected == "2":
            badge_reader_id = input("insert badge reader id: ")
            print(retrieve_badge_reader(session = session, badge_reader_id = badge_reader_id))

        elif crud_selected == "3":
            badge_reader_id = int(input("insert badge reader id: "))
            label_selected = input("insert badge reader label: ")
            sector_id_selected = int(input("insert sector id: "))
            badge_reader_info = {"label": label_selected, "sector_id": sector_id_selected}
            print(update_badge_reader(session = session, badge_reader_id = badge_reader_id, badge_reader_info = badge_reader_info))

        elif crud_selected == "4":
            badge_reader_id = input("insert badge reader id: ")
            print(delete_badge_reader(session = session, badge_reader_id = badge_reader_id))

        elif crud_selected == "0": break
        else: print("ERROR")
