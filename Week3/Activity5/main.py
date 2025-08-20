"""
Week 3 - Activity 5: update the sample code "Sample_code_SQLite3"
MSE800
270765080 Kristine Gonzalvo
Please add a new table named "Students" with three columns: Stu_ID, Stu_name, and Stu_address. 
Insert two sample records into Students, then display all rows from both the Users and Students tables.
"""

from database import create_table, create_table_student
from user_manager import add_user, view_users, search_user, delete_user
from student_manager import add_student, view_students, search_student, delete_student

def menu():
    print("\n==== User Manager ====")
    print("  1. Add User")
    print("  2. View All Users")
    print("  3. Search User by Name")
    print("  4. Delete User by ID")
    #print("5. Exit")
    print("==== Student Manager ====")
    print("  5. Add Student")
    print("  6. View All Students")
    print("  7. Search Student by Name")
    print("  8. Delete Student by ID")
    print("==== Other options ====")
    print("  9. Exit")

def main():
    create_table()
    create_table_student()
    while True:
        menu()
        choice = input("Select an option (1-9): ")
        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            add_user(name, email)
        elif choice == '2':
            users = view_users()
            print("\nAll Users:")
            for user in users:
                print(user)
        elif choice == '3':
            name = input("Enter name to search: ")
            users = search_user(name)
            for user in users:
                print(user)
        elif choice == '4':
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)
        elif choice == '5':
            name = input("Enter student's name: ")
            email = input("Enter student's email address: ")
            add_student(name, email)
        elif choice == '6':
            students = view_students()
            print("\nAll Students:")
            for student in students:
                print(student)
        elif choice == '7':
            name = input("Enter student's name to search: ")
            students = search_student(name)
            for student in students:
                print(student)
        elif choice == '8':
            student_id = int(input("Enter student ID to delete: "))
            delete_student(student_id)
        #elif choice == '5':
        elif choice == '9':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
