class AttendanceTracker:
    def __init__(self):
        self.students = []   # list of student names
        self.attendance = {} # { "student": "Present/Absent" }

    def add_student(self, name):
        if name not in self.students:
            self.students.append(name)
            print(f"✅ Student '{name}' added.")
        else:
            print("⚠️ Student already exists.")

    def mark_attendance(self):
        if not self.students:
            print("⚠️ No students available. Add students first!")
            return
        
        print("\nMark Attendance (P = Present, A = Absent)")
        for student in self.students:
            status = input(f"{student}: ").strip().upper()
            if status == "P":
                self.attendance[student] = "Present"
            else:
                self.attendance[student] = "Absent"
        print("✅ Attendance marked successfully!")

    def view_attendance(self):
        if not self.attendance:
            print("⚠️ No attendance records yet.")
            return

        print("\n===== Attendance Records =====")
        for student, status in self.attendance.items():
            print(f"{student} ➝ {status}")

def menu():
    tracker = AttendanceTracker()
    while True:
        print("\n===== ATTENDANCE TRACKER =====")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. View Attendance")
        print("4. Exit")

        choice = input("Choose option (1-4): ")

        if choice == "1":
            name = input("Enter student name: ")
            tracker.add_student(name)
        elif choice == "2":
            tracker.mark_attendance()
        elif choice == "3":
            tracker.view_attendance()
        elif choice == "4":
            print("👋 Exiting Attendance Tracker...")
            break
        else:
            print("❌ Invalid option, try again!")

# Run the app
menu()
