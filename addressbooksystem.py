from contacts import Contact
import pandas as pd


class AddressBookSystem:
    address_book_contacts = {}

    def create_contact(self):
        contact_dict = {
            "first_name": "",
            "last_name": "",
            "address": "",
            "city": "",
            "state": "",
            "zip": "",
            "phone_number": "",
            "email": ""
        }
        contact = Contact(contact_dict)
        contact = self.get_details(contact)
        return contact

    def get_details(self, contact):
        contact.first_name = input("Enter first name \n")
        contact.last_name = input("Enter last name \n")
        contact.address = input("Enter address \n")
        contact.city = input("Enter city \n")
        contact.state = input("Enter state \n")
        contact.zip = input("Enter zip code \n")
        contact.phone_number = input("Enter phone number \n")
        contact.email = input("Enter email address \n")
        return contact

    def add_contact(self):
        contact = self.create_contact()
        print("contact created")
        address_book_name = input("Enter the address book name \n")
        address_book = self.address_book_contacts.get(address_book_name)
        if address_book == None:
            contact_list = [contact]
            self.address_book_contacts[address_book_name] = contact_list
        else:
            address_book.append(contact)

    def display_contact(self):
        for address_book in self.address_book_contacts:
            contacts = "\n".join(str(contact) for contact in self.address_book_contacts.get(address_book))
            print(f"Contacts In {address_book} are \n{contacts}")

    def edit_contact(self):
        book_name = input("Enter the address book name ")
        address_book = self.address_book_contacts.get(book_name)
        if address_book != None:
            first_name = input("Enter the person name \n")
            contact_to_edit = [contact for contact in address_book if contact.first_name == first_name]
            if len(contact_to_edit) == 0:
                print("Contact not found")
            else:
                self.get_details(contact_to_edit[0])
                print("Contact Edited Sucessfully")
        else:
            print("No such address book")

    def delete_contact(self):
        book_name = input("Enter the address book name ")
        address_book = self.address_book_contacts.get(book_name)
        if address_book != None:
            first_name = input("Enter the person name \n")
            contact_to_delete = [contact for contact in address_book if contact.first_name == first_name]
            if len(contact_to_delete) == 0:
                print("Contact not found")
            else:
                address_book.remove(contact_to_delete[0])
                print("Contact removed sucessfully")
        else:
            print("No such address book")

    def write_in_csv(self):
        # with open("contactsdata.csv", "w") as f:
        #     for address_book in self.address_book_contacts:
        #         contacts = "\n".join(str(contact) for contact in self.address_book_contacts.get(address_book))
        #         f.write(f"Contacts in {address_book} are \n{contacts}")

        for address_book in self.address_book_contacts:
            contacts = "\n".join(str(contact) for contact in self.address_book_contacts.get(address_book))
            # f.write(f"Contacts in {address_book} are \n{contacts}")
            df = pd.DataFrame(list(f"Contacts in {address_book} are \n{contacts}\n"))
            df.to_csv('contactsdata.csv', mode='a', header=False, index=None)

