from data_manager import DataManager
import datetime as dt

TODAY = dt.datetime.today().date()
AHEAD = (TODAY + dt.timedelta(days=6 * 30))


ADD_USER = True

while ADD_USER:

    first_name = str(input("What is your first name? ")).title()
    last_name = str(input("What is your last name? ")).title()
    email = str(input("What is your email? "))

    datamanager = DataManager(sheet='users')
    new_data = {'firstName': first_name, 'lastName': last_name, 'email': email}
    datamanager.add_entry(new_data)


    end_edit = str(input("Add another user? 'y or 'n'"))

    if end_edit == 'n':
        ADD_USER = False
    elif end_edit == 'y':
        ADD_USER = True
    else:
        raise ValueError("Please reply with 'y' or 'n'")
