from models.person import Person

class Student(Person):
    def __init__(self, student_id, name, email, phone_number):
        super().__init__(name, email, phone_number)
        self.student_id = student_id
        students.append({'student_id': self.student_id, 'name': self.name, 'email': self.email, 'phone_number': self.phone_number})
        save_data()

    def __str__(self):
        return f"Student ID: {self.student_id}, Student Name: {self.name}, Phone Number:{self.phone_number}, Email: {self.email},"

    def search_for_students(self, search_name):
        check = [student for student in students if student['name'] == search_name or student['student_id'] == search_name]
        if check != []:
                print(check)
        else:
                print("Student not found.")
    
    def view_courses_for_student(self, student):
        if student in [student['student_id'] for student in students] or student in [student['name'] for student in students]:
            courses_for_student = [registration['course_applied'] for registration in registrations if registration['name'] == student]
            print(f"Courses for {student}: {courses_for_student}")
        else:
            print("Student not found.Try again with student ID")