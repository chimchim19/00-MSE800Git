"""
Week 3 - Activity 6: Develop the python code for Week 3 - Activity 4
MSE800
270765080 Kristine Gonzalvo
Use the sample code to develop a command-line application for Week 3 - Activity 4,
incorporating a database sqlite3 and have at least three functionality such as add records,
delete records and view records for different tables.
"""

import sqlite3

def create_connection():
    conn = sqlite3.connect("Week3/Activity6/yoobee.db")
    return conn

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()
    
    # Program table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Program (
            Program_ID TEXT PRIMARY KEY NOT NULL,
            Program_Code TEXT NOT NULL,
            Program_Desc TEXT NOT NULL
        )
    ''')

    # Course table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Course (
            Course_Code TEXT PRIMARY KEY NOT NULL,
            Course_Desc TEXT NOT NULL
        )
    ''')

    # Student table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Student (
            Student_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Last_Name TEXT NOT NULL,
            First_Name TEXT NOT NULL,
            Email TEXT NOT NULL UNIQUE,
            Program_ID TEXT NOT NULL,
            FOREIGN KEY(Program_ID) REFERENCES Program(Program_ID)
        )
    ''')

    # Lecturer table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Lecturer (
            Lecturer_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Last_Name TEXT NOT NULL,
            First_Name TEXT NOT NULL,
            Email TEXT NOT NULL UNIQUE
        )
    ''')

    # Class table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ClassTab (
            Class_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Program_ID TEXT NOT NULL,
            Course_Code TEXT NOT NULL,
            Lecturer_ID INTEGER NOT NULL,
            FOREIGN KEY(Program_ID) REFERENCES Program(Program_ID),
            FOREIGN KEY(Course_Code) REFERENCES Course(Course_Code)
        )
    ''')

    conn.commit()
    conn.close()
    