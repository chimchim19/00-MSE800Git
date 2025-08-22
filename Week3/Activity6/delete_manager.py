"""
Week 3 - Activity 6: Develop the python code for Week 3 - Activity 4
MSE800
270765080 Kristine Gonzalvo
Use the sample code to develop a command-line application for Week 3 - Activity 4,
incorporating a database sqlite3 and have at least three functionality such as add records,
delete records and view records for different tables.
"""

from database import create_connection

def delete_program(id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Program WHERE Program_ID = ?", (id,))
    conn.commit()
    conn.close()
    print("🗑️ Program deleted.")

def delete_course(code):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Course WHERE Course_Code = ?", (code,))
    conn.commit()
    conn.close()
    print("🗑️ Course deleted.")

def delete_lecturer(id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Lecturer WHERE Lecturer_ID = ?", (id,))
    conn.commit()
    conn.close()
    print("🗑️ Lecturer deleted.")

def delete_student(id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Student WHERE Student_ID = ?", (id,))
    conn.commit()
    conn.close()
    print("🗑️ Student deleted.")

def delete_class(id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ClassTab WHERE Class_ID = ?", (id,))
    conn.commit()
    conn.close()
    print("🗑️ Class deleted.")