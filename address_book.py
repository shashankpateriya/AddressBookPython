import logging
import json
import pandas
from contacts import Contact
from addressbooksystem import AddressBookSystem

logging.basicConfig(
    filename="addressbooklogger.log",
    filemode="a",
    format="%(asctime)s %(levelname)s-%(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
log = logging.getLogger()

if __name__ == '__main__':

    console_service = AddressBookSystem()
    print("Welcome to Address Book Management System")

    while True:
        user_choice = ""
        while user_choice != "q":
            print("1 - Enter a contact")
            print("2 - Display contacts")
            print("3 - Edit a contact")
            print("4 - Delete a contact")
            print("q - quit program")
            try:
                user_choice = input("Select option: ")
                if user_choice == "1":
                    console_service.add_contact()

                elif user_choice == "2":
                    console_service.display_contact()

                elif user_choice == "3":
                    console_service.edit_contact()

                elif user_choice == "4":
                    console_service.delete_contact()

                elif user_choice == "q":
                    print("Thanks for using us ")
                    exit()
                else:
                    log.warning("Choose a option from 1 to 5")
            except Exception as e:
                raise ValueError
