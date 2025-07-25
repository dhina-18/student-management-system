from students import add_student, view_students, delete_student
from marks import add_mark, view_marks
from subjects import add_subject, view_subjects

def main():
    while True:
        print("\n=== Student Management System ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Add Mark")
        print("4. View Marks")
        print("5. Delete Student")
        print("6. Add Subject")
        print("7. View Subjects")
        print("8. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Name: ")
            gender = input("Gender (Male/Female/Other): ")
            dob = input("Date of Birth (YYYY-MM-DD): ")
            class_name = input("Class Name: ")
            add_student(name, gender, dob, class_name)
        elif choice == '2':
            view_students()
        elif choice == '3':
            student_id = int(input("Enter Student ID: "))
            subject_id = int(input("Enter Subject ID: "))
            marks = int(input("Enter Marks: "))
            add_mark(student_id, subject_id, marks)
        elif choice == '4':
            view_marks()
        elif choice == '5':
            student_id = int(input("Enter Student ID to delete: "))
            delete_student(student_id)
        elif choice == '6':
            subject_name = input("Enter Subject Name: ")
            add_subject(subject_name)
        elif choice == '7':
            view_subjects()
        elif choice == '8':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()