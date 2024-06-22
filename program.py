import json

class AttendanceSystem:
    def __init__(self):
        try:
            with open('attendance_data.json', 'r') as file:
                self.attendance_list = json.load(file)
        except FileNotFoundError:
            self.attendance_list = {}

    def add_student(self, student_id, name, classe):
        self.attendance_list[student_id] = {'name': name, 'classe': classe, 'attendance': []}
        self.save_data()

    def mark_attendance(self, student_id, is_present, cours):
        if student_id in self.attendance_list:
            if is_present:
                self.attendance_list[student_id]['attendance'].append({'cours': cours, 'status': 'Present'})
            else:
                self.attendance_list[student_id]['attendance'].append({'cours': cours, 'status': 'Absent'})
            self.save_data()
        else:
            print("Student not found.")

    def view_attendance_list(self):
        print("Attendance List:")
        for student_id, details in self.attendance_list.items():
            print(f"Student ID: {student_id}, Name: {details['name']}, Classe: {details['classe']}, Attendance: {details['attendance']}")

    def search_student(self, name):
        for student_id, details in self.attendance_list.items():
            if details['name'] == name:
                print(f"Student ID: {student_id}, Name: {details['name']}, Classe: {details['classe']}, Attendance: {details['attendance']}")
                return
        print("Student not found.")

    def save_data(self):
        with open('attendance_data.json', 'w') as file:
            json.dump(self.attendance_list, file, indent=4)

def main():
    attendance_system = AttendanceSystem()

    while True:
        print("\n1. Add Student")
        print("2. Mark Attendance")
        print("3. View Attendance List")
        print("4. Search Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            student_id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            classe = input("Enter Student Class: ")
            attendance_system.add_student(student_id, name, classe)
            print("Student added successfully.")

        elif choice == '2':
            student_id = input("Enter Student ID: ")
            is_present = input("Is the student present? (yes/no): ").lower()
            cours = input("Enter the course name: ")
            if is_present == 'yes':
                attendance_system.mark_attendance(student_id, True, cours)
            elif is_present == 'no':
                attendance_system.mark_attendance(student_id, False, cours)
            else:
                print("Invalid input.")

        elif choice == '3':
            attendance_system.view_attendance_list()

        elif choice == '4':
            name = input("Enter student name to search: ")
            attendance_system.search_student(name)

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
