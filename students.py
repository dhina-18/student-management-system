from db_config import get_connection

def add_student(name, gender, dob, class_name):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO students (name, gender, dob, class_name) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (name, gender, dob, class_name))
    conn.commit()
    print("Student added successfully.")
    cursor.close()
    conn.close()

def view_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    conn.close()

def delete_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM students WHERE student_id = %s"
    cursor.execute(query, (student_id,))
    conn.commit()
    if cursor.rowcount > 0:
        print("Student deleted successfully.")
    else:
        print("Student ID not found.")
    cursor.close()
    conn.close()