# studentreport.py
# Module for generating and displaying student reports
# Author: Tasawar Ali

from addstudent import StudentManager
from addcourse import CourseManager

class ReportManager:
    def _init_(self):
        self.student_manager = StudentManager()
        self.course_manager = CourseManager()

    def generate_student_report(self):
        print("\n===== 📋 Student Report =====")

        if not self.student_manager.students:
            print("⚠️ No students available to display.")
            return

        for student in self.student_manager.students:
            print(f"\nStudent ID: {student['id']}")
            print(f"Name      : {student['name']}")
            print(f"Course ID : {student['course_id']}")
                 # Find the course name from course list
            course = next((c for c in self.course_manager.courses if c["id"] == student["course_id"]), None)
            if course:
                print(f"Course Name: {course['name']}")
                print(f"Instructor : {course['instructor']}")
            else:
                print("Course details not found.")
        print("=================================")


if _name_ == "_main_":
    report_manager = ReportManager()
    report_manager.generate_student_report()