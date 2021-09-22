class Contact:
    def __init__(self, contact):
        self.first_name = contact.get("first_name")
        self.last_name = contact.get("last_name")
        self.address = contact.get("address")
        self.city = contact.get("city")
        self.state = contact.get("state")
        self.zip = contact.get("zip")
        self.phone_number = contact.get("phone_number")
        self.email = contact.get("email")

    def __str__(self):
        return f"First name : {self.first_name} \nLast name : {self.last_name} \nAddress : {self.address} \n" \
               f"City : {self.city} \nState : {self.state} \nZip : {self.zip} \n"
