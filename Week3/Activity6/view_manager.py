"""
Week 3 - Activity 6: Develop the python code for Week 3 - Activity 4
MSE800
270765080 Kristine Gonzalvo
Use the sample code to develop a command-line application for Week 3 - Activity 4,
incorporating a database sqlite3 and have at least three functionality such as add records,
delete records and view records for different tables.
"""

from database import create_connection

def view_classes():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ClassTab")
    rows = cursor.fetchall()
    conn.close()
    return rows

def view_programs():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Program")
    rows = cursor.fetchall()
    conn.close()
    return rows

def view_courses():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Course")
    rows = cursor.fetchall()
    conn.close()
    return rows

def view_lecturers():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Lecturer")
    rows = cursor.fetchall()
    conn.close()
    return rows

def view_students():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Student")
    rows = cursor.fetchall()
    conn.close()
    return rows
