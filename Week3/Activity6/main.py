"""
Week 3 - Activity 6: Develop the python code for Week 3 - Activity 4
MSE800
270765080 Kristine Gonzalvo
Use the sample code to develop a command-line application for Week 3 - Activity 4,
incorporating a database sqlite3 and have at least three functionality such as add records,
delete records and view records for different tables.
"""

from database import create_tables
from view_manager import view_classes, view_programs, view_courses, view_lecturers, view_students
from add_manager import add_class, add_program, add_course, add_lecturer, add_student
from delete_manager import delete_class, delete_program, delete_course, delete_lecturer, delete_student

def menu():
    print("\n==== View Options ====")
    print("  1. View Classes")
    print("  2. View Programs")
    print("  3. View Courses")
    print("  4. View Lecturers")
    print("  5. View Students")
    print("==== Add Options ====")
    print("  6. Add Class")
    print("  7. Add Program")
    print("  8. Add Course")
    print("  9. Add Lecturer")
    print("  10. Add Student")
    print("==== Delete Options ====")
    print("  11. Delete Class")
    print("  12. Delete Program")
    print("  13. Delete Course")
    print("  14. Delete Lecturer")
    print("  15. Delete Student")
    print("==== Other options ====")
    print("  16. Exit")

def main():
    create_tables()
    while True:
        menu()
        choice = input("Select an option (1-16): ")
        if choice == '1':
            classes = view_classes()
            print("\nAll Classes:")
            for cl in classes:
                print(cl)
        elif choice == '2':
            programs = view_programs()
            print("\nAll Programs:")
            for prog in programs:
                print(prog)
        elif choice == '3':
            courses = view_courses()
            print("\nAll Courses:")
            for course in courses:
                print(course)
        elif choice == '4':
            lecturers = view_lecturers()
            print("\nAll Lecturers:")
            for lecturer in lecturers:
                print(lecturer)
        elif choice == '5':
            students = view_students()
            print("\nAll Students:")
            for student in students:
                print(student)
        elif choice == '6':
            program = input("Enter Program ID of the Class: ")
            course = input("Enter Course Code of the Class: ")
            lecturer = int(input("Enter ID of lecturer to be assigned: "))
            add_class(program, course, lecturer)
        elif choice == '7':
            id = input("Enter unique ID for the program(<code><yy><mm><section>): ")
            code = input("Enter the program code: ")
            desc = input("Enter the program description: ")
            add_program(id, code, desc)
        elif choice == '8':
            code = input("Enter unique code for the course: ")
            desc = input("Enter short description for the course: ")
            add_course(code, desc)
        elif choice == '9':
            name1 = input("Enter Last Name: ")
            name2 = input("Enter First Name: ")
            email = input("Enter email: ")
            add_lecturer(name1, name2, email)
        elif choice == '10':
            name1 = input("Enter Last Name: ")
            name2 = input("Enter First Name: ")
            email = input("Enter email: ")
            program = input("Enter Program ID that student is enrolled to: ")
            add_student(name1, name2, email, program)
        elif choice == '11':
            class_id = int(input("Enter ID of Class to delete: "))
            delete_class(class_id)
        elif choice == '12':
            program_id = input("Enter ID of program to be deleted: ")
            delete_program(program_id)
        elif choice == '13':
            course_code = input("Enter code of course to be deleted: ")
            delete_course(course_code)
        elif choice == '14':
            lecturer_id = int(input("Enter ID of lecturer to be deleted: "))
            delete_lecturer(lecturer_id)
        elif choice == '15':
            student_id = int(input("Enter ID of student to be deleted: "))
            delete_student(student_id)
        elif choice == '16':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
