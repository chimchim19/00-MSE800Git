"""
Week 3 - Activity 5: update the sample code "Sample_code_SQLite3"
MSE800
270765080 Kristine Gonzalvo
Please add a new table named "Students" with three columns: Stu_ID, Stu_name, and Stu_address. 
Insert two sample records into Students, then display all rows from both the Users and Students tables.
"""

import sqlite3

def create_connection():
    #conn = sqlite3.connect("users.db")
    conn = sqlite3.connect("Week3/Activity5/users.db")
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    conn.close()

# add table Students in database users.db
def create_table_student():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Students (
            Stu_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Stu_name TEXT NOT NULL,
            Stu_address TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    conn.close()
