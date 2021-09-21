class Contact:
    def __init__(self, first_name, last_name, address, city, state, zip, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"First name : {self.first_name} \nLast name : {self.last_name} \nAddress : {self.address} \n" \
               f"City : {self.city} \nState : {self.state} \nZip : {self.zip} \n" \
               f"Phone number : {self.phone_number} \nEmail: {self.email}"