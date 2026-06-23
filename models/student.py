from models.person import Person

class Student(Person):
    def __init__(self, name, email, phone_number):
        super().__init__(name, email, phone_number)

#Student management methods
    # ---------------adds a student 
    # ---------------view students 
    # ---------------update student
    # ---------------search student
    # ---------------delete student