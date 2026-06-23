class SchoolSystem:
    def __init__(self, students, courses, registrations):

        self.students = students
        self.courses = courses
        self.registrations = registrations
        self.applications = []
    
    
# Helper Methods
    # ---------------Email check
      # if "@" and ".com" not in email:
      #         print("Please enter a valid email format")
    # ---------------check if student exists
    # ---------------students in a courses
    # ---------------available slots
    # ---------------create folder if missing
    

    # Registrations management methods 

    # view students in course 
    # view courses for a student 
    # register student to course
    # students in that courses + available costs

    # report

    # file handling
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
    # display menu

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
            phone_number = input("Enter the phone number of the student: eg. +25454738573 ")
            ##
            print("Student added successfully.")
        
        elif choice == '2':
            print("All students:")
            for student in students:
                print(student)
        
        elif choice == '3':
            search_name = input("Enter name or student ID of the student: ")
            ##

        elif choice == '4':
            course_id = input("Enter the course ID: ")
            course_name = input("Enter the course name: ")
            trainer_name = input("Enter the trainer name: ")
            capacity = int(input("Enter the capacity of the course: "))
            for course in courses:
                if course_name == course['course_name']:
                    print("Course is already present")
            ##

        elif choice == '5':
            print("All courses:")
            ##
        
        elif choice == '6':
            student = input("Enter the student ID or name: ")
            course = input("Enter the course ID or name: ")
            ##

        elif choice == '7':
            course = input("Enter the course ID or name: ")
            ##
        
        elif choice == '8':
            student = input("Enter the student ID or name: ")
            ##
        
        elif choice == '9':
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            if "@" or ".com" not in email:
                print("Please enter a valid email format")
                email = input("Enter a correct email eg.(example@gmail.com) ")
                phone_number = input("Enter your phone number: eg. +25454738573 ")
                ##
                print("Your details have been submitted")
            else:
                phone_number = input("Enter your phone number: eg. +25454738573 ")
                ##
                print("Your details have been submitted")

        elif choice == '10':
            print("Applications:")
            

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
