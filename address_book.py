from contacts import Contact

if __name__ == '__main__':
    contacts = []
    user_input = ""
    while user_input != "q":
        print("1 - Enter a contact")
        print("2 - Display contacts")
        print("3 - Edit a contact")
        print("q - quit program")
        user_input = input("Select option: ")
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
            to_lookup = input("Enter contact's name to lookup\n")
            for contact in contacts:
                if to_lookup in contact.full_name():
                    new_first_name = input("Enter first name \n")
                    new_last_name = input("Enter last name \n")
                    new_address = input("Enter address \n")
                    new_city = input("Enter city \n")
                    new_state = input("Enter state \n")
                    new_zip = input("Enter zip code \n")
                    new_phone_number = input("Enter phone number \n")
                    new_email = input("Enter email address \n")
                    new_contact = Contact(new_first_name, new_last_name, new_address, new_city, new_state,
                                      new_zip, new_phone_number, new_email)
                    contacts.append(new_contact)
        elif user_input == "4":
            to_delete = input("Enter contact's name to lookup\n")
            for contact in contacts:
                if to_delete in contact.full_name():
                    contacts.remove(contact)
        else:
            break
