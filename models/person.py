class Person:
    def __init__(self, name, email, phone_number, role):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.role = role

        #add to applications
    
    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Phone Number: {self.phone_number}"