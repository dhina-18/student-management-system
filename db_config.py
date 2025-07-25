import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Dhinakarvirat@18",
        database="student_management"
    )