if __name__ == '__main__':
    user_input = ""
    while user_input != "q":
        print("1 - Enter a contact")
        print("2 - Display contacts")
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
        else:
            break
