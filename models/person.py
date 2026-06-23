class Person:
    def __init__(self, name, email, phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        # SchoolSystem.applications.append(self)
        # save_data()
    
    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Phone Number: {self.phone_number}"