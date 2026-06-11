students = []
courses = []
registrations = []

# ---------------------------NEW APPLICATIONS--------------------------------
# Name
# Email
# Phone number

class Person:
    def __init__(self, name, email, phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        # SchoolSystem.applications.append(self)
        save_data()
    
    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Phone Number: {self.phone_number}"

# --------------------------STUDENTS------------------------------------
# Student ID
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
# ----------------------COURSES (Active participants & courses)----------------------------------------
# Course ID
# Course name
# Trainer name
# Capacity

class Course:
    def __init__(self, course_id, course_name, trainer_name, capacity):
        self.course_id = course_id
        self.course_name = course_name
        self.trainer_name = trainer_name
        self.capacity = int(capacity)
        courses.append({'course_id': self.course_id, 'course_name': self.course_name, 'trainer_name': self.trainer_name, 'capacity': self.capacity})
        save_data()

    def __str__(self):
        return f"Course ID: {self.course_id}, Course Name: {self.course_name}, Trainer Name: {self.trainer_name}, Capacity: {self.capacity}"

    def view_all_courses(self):
        for course in courses:
                print(course)

    def view_students_in_course(self, course):
        if course in [course['course_id'] for course in courses] or course in [course['course_name'] for course in courses]:
            students_in_course = [registration['name'] for registration in registrations if registration['course_applied'] == course]
            print(f"Students in {course}: {students_in_course}")
        else:
                print("Course not found.")

# -------------------------SCHOOL SYSTEM (Registrations, Applications)-------------------------------------
class SchoolSystem:
    def __init__(self):

        self.students = students
        self.courses = courses
        self.registrations = registrations
        self.applications = []
    
    def add_student(self, student_id, name, email, phone_number):
        new_student = Student(student_id, name, email, phone_number)
        save_data()

    def add_course(self, course_id, course_name, trainer_name, capacity):
        num_courses = len(courses)
        new_course = Course(course_id, course_name, trainer_name, capacity)

        if len(courses) > num_courses:
            print("Course added successfully.")
        else:
            print("Course was not added. Please try again.")
        save_data()

    def register_student(self, student, course):
        if student in [student['student_id'] for student in students] or student in [student['name'] for student in students]:
        
            if course in [course['course_id'] for course in courses] or course in [course['course_name'] for course in courses]:
                registrations.append({'name': student, 'course_applied': course, 'registration_status': 'Approved'})
                print("Student registered to the course successfully.")
            else:
                print("Course not found.")
        else:
                print("Student not found.")
        save_data()

# ---------------------------DATA---------------------------------

import json
import os

students_file = 'students.json'
courses_file = 'courses.json'
registrations_file = 'registrations.json'

def load_data():
    global students, courses, registrations

    if os.path.exists(students_file):
        with open(students_file, 'r') as f:
            students = json.load(f)
    
    if os.path.exists(courses_file):
        with open(courses_file, 'r') as f:
            courses = json.load(f)
    
    if os.path.exists(registrations_file):
        with open(registrations_file, 'r') as f:
            registrations = json.load(f)

    print(f"{len(students)} students, {len(courses)} courses, {len(registrations)} registrations.")

def save_data():
    with open(students_file, 'w') as f:
        json.dump(students, f)
            
    with open(courses_file, 'w') as f:
        json.dump(courses, f)
    
    with open(registrations_file, 'w') as f:
        json.dump(registrations, f)

# Load existing data on startup so new additions append to existing files
load_data()

try:
    while True:
        print("===== Admin System =====")
        print("")
        print("")
        print("1. Add student")
        print("2. View students")
        print("3. Search student")
        print("4. Add course")
        print("5. View courses")
        print("6. Register student to a course")
        print("7. View students in a course")
        print("8. View courses for a student")
        print("9. Apply to the school")
        print("10. View applications --upcoming feature")
        print("11. Save data")
        print("12. Load data")
        print("0. Exit")
        print("")
        print("")
        
        choice = input("Choose an option: eg. 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 or 0: ")

        if choice == '1':
            student_id = input("Enter the new student ID: ")
            name = input("Enter the name of the student: ")
            email = input("Enter the email of the student: ")
            if "@" and ".com" not in email:
                print("Please enter a valid email format")
                email = input("Enter a correct email eg.(example@gmail.com)")
            phone_number = input("Enter the phone number of the student: eg. +25454738573 ")
            SchoolSystem.add_student(SchoolSystem, student_id, name, email, phone_number)
            print("Student added successfully.")
        
        elif choice == '2':
            print("All students:")
            for student in students:
                print(student)
        
        elif choice == '3':
            search_name = input("Enter name or student ID of the student: ")
            Student.search_for_students(Student, search_name)

        elif choice == '4':
            course_id = input("Enter the course ID: ")
            course_name = input("Enter the course name: ")
            trainer_name = input("Enter the trainer name: ")
            capacity = int(input("Enter the capacity of the course: "))
            for course in courses:
                if course_name == course['course_name']:
                    print("Course is already present")
            SchoolSystem.add_course(SchoolSystem, course_id, course_name, trainer_name, capacity)

        elif choice == '5':
            print("All courses:")
            Course.view_all_courses(Course)
        
        elif choice == '6':
            student = input("Enter the student ID or name: ")
            course = input("Enter the course ID or name: ")
            SchoolSystem.register_student(SchoolSystem, student, course)

        elif choice == '7':
            course = input("Enter the course ID or name: ")
            Course.view_students_in_course(Course, course)
        
        elif choice == '8':
            student = input("Enter the student ID or name: ")
            Student.view_courses_for_student(Student, student)
        
        elif choice == '9':
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            if "@" or ".com" not in email:
                print("Please enter a valid email format")
                email = input("Enter a correct email eg.(example@gmail.com) ")
                phone_number = input("Enter your phone number: eg. +25454738573 ")
                Person(name, email, phone_number)
                print("Your details have been submitted")
            else:
                phone_number = input("Enter your phone number: eg. +25454738573 ")
                Person(name, email, phone_number)
                print("Your details have been submitted")

        # elif choice == '10':
        #     print("Applications:")
        #     for person in [person for person in SchoolSystem.applications if isinstance(person, Person) and not isinstance(person, Student)]:
        #         print(person)

        elif choice == '11':
            save_data()
            print("Data saved successfully.")
        
        elif choice == '12':
            load_data()
            print("Data loaded successfully.")

        elif choice == '0':
            save_data()
            break
        else:
            print("Invalid choice. Please try again.")

finally:
    save_data()

