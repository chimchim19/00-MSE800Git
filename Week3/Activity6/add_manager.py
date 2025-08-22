"""
Week 3 - Activity 6: Develop the python code for Week 3 - Activity 4
MSE800
270765080 Kristine Gonzalvo
Use the sample code to develop a command-line application for Week 3 - Activity 4,
incorporating a database sqlite3 and have at least three functionality such as add records,
delete records and view records for different tables.
"""

from database import create_connection
import sqlite3

def add_program(id, code, desc):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Program (Program_ID, Program_Code, Program_Desc) VALUES (?, ?, ?)", (id, code, desc))
        conn.commit()
        print(" Program added successfully.")
    except sqlite3.IntegrityError as error:
        print(f"Error adding program: {error}")
    except sqlite3.Error as error:
        print(f"Error adding program: {error}")
    conn.close()

def add_course(code, desc):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Course (Course_Code, Course_Desc) VALUES (?, ?)", (code, desc))
        conn.commit()
        print(" Course added successfully.")
    except sqlite3.IntegrityError as error:
        print(f"Error adding course: {error}")
    except sqlite3.Error as error:
        print(f"Error adding course: {error}")
    conn.close()

def add_lecturer(name1, name2, email):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Lecturer (Last_Name, First_Name, Email) VALUES (?, ?, ?)", (name1, name2, email))
        conn.commit()
        print(" Lecturer added successfully.")
    except sqlite3.IntegrityError:
        print(" Email must be unique.")
    conn.close()

def add_student(name1, name2, email, program):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""INSERT INTO Student (Last_Name, First_Name, Email, Program_ID)
                                VALUES (?, ?, ?, ?)""", (name1, name2, email, program))
        conn.commit()
        print(" Student added successfully.")
    except sqlite3.IntegrityError:
        print(" Email must be unique.")
    except sqlite3.Error as error:
        print(f"Error adding student: {error}")
    conn.close()

def add_class(program, course, lecturer):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""INSERT INTO ClassTab (Program_ID, Course_Code, Lecturer_ID)
                                VALUES (?, ?, ?)""", (program, course, lecturer))
        conn.commit()
        print(" Class added successfully.")
    except sqlite3.IntegrityError as error:
        print(f"Error adding class: {error}")
    except sqlite3.Error as error:
        print(f"Error adding class: {error}")
    conn.close()