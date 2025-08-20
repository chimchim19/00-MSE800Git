"""
Week 3 - Activity 5: update the sample code "Sample_code_SQLite3"
MSE800
270765080 Kristine Gonzalvo
Please add a new table named "Students" with three columns: Stu_ID, Stu_name, and Stu_address. 
Insert two sample records into Students, then display all rows from both the Users and Students tables.
"""

from database import create_connection
import sqlite3

def add_student(name, email):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Students (Stu_name, Stu_address) VALUES (?, ?)", (name, email))
        conn.commit()
        print(" Student added successfully.")
    except sqlite3.IntegrityError:
        print(" Email must be unique.")
    conn.close()

def view_students():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Students")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_student(name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Students WHERE Stu_name LIKE ?", ('%' + name + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_student(student_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Students WHERE Stu_ID = ?", (student_id,))
    conn.commit()
    conn.close()
    print("🗑️ Student deleted.")
