# addcourse.py
# This module handles adding new courses in the student management system.

class Course:
    def __init__(self, course_id, name, instructor):
        self.course_id = course_id
        self.name = name
        self.instructor = instructor

    def __str__(self):
        return f"Course ID: {self.course_id}, Name: {self.name}, Instructor: {self.instructor}"


class CourseManager:
    def __init__(self):
        self.courses = []

    def add_course(self, course_id, name, instructor):
        # Check if course already exists
        for course in self.courses:
            if course.course_id == course_id:
                print(f"⚠️ Course ID '{course_id}' already exists!")
                return

        new_course = Course(course_id, name, instructor)
        self.courses.append(new_course)
        print(f"✅ Course '{name}' added successfully!")

    def display_courses(self):
        if not self.courses:
            print("No courses found!")
        else:
            print("\n📚 List of Courses:")
            for course in self.courses:
                print(course)


# Only runs if file is executed directly (not imported)
if __name__ == "__main__":
    manager = CourseManager()

    while True:
        print("\n--- Add Course Menu ---")
        print("1. Add New Course")
        print("2. View All Courses")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            course_id = input("Enter Course ID: ")
            name = input("Enter Course Name: ")
            instructor = input("Enter Instructor Name: ")
            manager.add_course(course_id, name, instructor)

        elif choice == "2":
            manager.display_courses()

        elif choice == "3":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice! Try again.")
