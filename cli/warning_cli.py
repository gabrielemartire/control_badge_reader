from actions.crud_warning import create_warning, retrieve_warning, update_warning, delete_warning 

def warning_submenu(session):
    while True:
        print("available actions:")
        print("1 - create new warning")
        print("2 - retrieve warning")
        print("3 - update warning")
        print("4 - delete warning")
        print("0 - back")

        crud_selected = int(input("select action: "))

        match crud_selected:
            case 1:
                code_name_selected = input("insert warning code name: ")
                descr_selected = input("insert warning description: ")
                new_role_dict = {"code_name": code_name_selected, "description": descr_selected}
                print(create_warning(session = session, warning_info = new_role_dict))

            case 2:
                warning_id = int(input("insert insert warning id: "))
                print(retrieve_warning(session = session, warning_id = warning_id))

            case 3:
                warning_id = int(input("insert warning id: "))
                code_name_selected = input("insert warning code name: ")
                descr_selected = input("insert warning description: ")
                upd_warning_dict = {"code_name": code_name_selected, "description": descr_selected}
                print(update_warning(session = session, warning_id = warning_id, warning_info = upd_warning_dict))

            case 4:
                warning_id = int(input("insert warning id: "))
                print(delete_warning(session = session, warning_id = warning_id))

            case 0: break

            case _: print("ERROR")
