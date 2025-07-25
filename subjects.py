from db_config import get_connection

def add_subject(subject_name):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        query = "INSERT INTO subjects (subject_name) VALUES (%s)"
        cursor.execute(query, (subject_name,))
        conn.commit()
        print(f"Subject '{subject_name}' added successfully.")
    except Exception as e:
        print(f"Error adding subject: {e}")
    finally:
        cursor.close()
        conn.close()

def view_subjects():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM subjects")
    subjects = cursor.fetchall()
    if subjects:
        print("\nSubjects List:")
        for sub in subjects:
            print(f"ID: {sub[0]} | Name: {sub[1]}")
    else:
        print("No subjects found.")
    cursor.close()
    conn.close()
