import logging
import pandas
from contacts import Contact

logging.basicConfig(
    filename="addressbooklogger.log",
    filemode="a",
    format="%(asctime)s %(levelname)s-%(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
log = logging.getLogger()


if __name__ == '__main__':
    contacts = []
    user_input = ""
    while user_input != "q":
        print("1 - Enter a contact")
        print("2 - Display contacts")
        print("3 - Edit a contact")
        print("4 - Delete a contact")
        print("q - quit program")
        user_input = input("Select option: ")
        try:
            if user_input == "1":
                print("Enter contact information")
                first_name = input("Enter first name \n")
                last_name = input("Enter last name \n")
                address = input("Enter address \n")
                city = input("Enter city \n")
                state = input("Enter state \n")
                zip = input("Enter zip code \n")
                phone_number = input("Enter phone number \n")
                email = input("Enter email address \n")

                our_contact = Contact(first_name, last_name, address, city, state, zip, phone_number, email)
                contacts.append(our_contact)
            elif user_input == "2":
                for contact in contacts:
                    print(contact)
            elif user_input == "3":
                to_lookup = input("Enter contact's full name to delete\n")
                for contact in contacts:
                    if to_lookup in contact.full_name():
                        first_name = input("Enter new first name \n")
                        last_name = input("Enter new last name \n")
                        address = input("Enter new address \n")
                        city = input("Enter new city \n")
                        state = input("Enter new state \n")
                        zip = input("Enter new zip code \n")
                        phone_number = input("Enter new phone number \n")
                        email = input("Enter new email address \n")
                        new_contact = Contact(first_name, last_name, address, city, state, zip, phone_number, email)
                        contacts.append(new_contact)
            elif user_input == "4":
                to_delete = input("Enter contact's name to lookup\n")
                for contact in contacts:
                    if to_delete in contact.full_name():
                        contacts.remove(contact)
            elif user_input == "":
                log.warning("No input was given")
            elif user_input == "q":
                break
        except Exception as e:
            raise ValueError

        with open("contactsdata.csv", "w") as f:
            for contact in contacts:
                f.write(f"{contact.first_name},{contact.last_name},{contact.address},{contact.city},{contact.state}"
                        f"{contact.zip},{contact.phone_number},{contact.email}\n")
