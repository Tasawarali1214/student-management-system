# addstudent.py
# Module for managing student data
# Author: Tasawar Ali

class Student:
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course

    def __str__(self):
        return f"🎓 ID: {self.student_id} | Name: {self.name} | Course: {self.course}"


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student_id, name, course):
        # Check if ID already exists
        for s in self.students:
            if s.student_id == student_id:
                print("⚠️ Student ID already exists! Please use a different ID.")
                return
        new_student = Student(student_id, name, course)
        self.students.append(new_student)
        print(f"✅ Student '{name}' added successfully!")

    def display_students(self):
        if not self.students:
            print("❌ No students found!")
        else:
            print("\n===== Student List =====")
            for student in self.students:
                print(student)
