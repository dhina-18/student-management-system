from db_config import get_connection

def add_mark(student_id, subject_id, marks):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO marks (student_id, subject_id, marks) VALUES (%s, %s, %s)"
    cursor.execute(query, (student_id, subject_id, marks))
    conn.commit()
    print("Mark added successfully.")
    cursor.close()
    conn.close()

def view_marks():
    conn = get_connection()
    cursor = conn.cursor()
    query = '''
        SELECT s.name, sub.subject_name, m.marks
        FROM marks m
        JOIN students s ON m.student_id = s.student_id
        JOIN subjects sub ON m.subject_id = sub.subject_id
    '''
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    conn.close()