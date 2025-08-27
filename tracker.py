# tracker.py

class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.grades = {}  # Dictionary to store subject: grade

    def add_grade(self, subject, score):
        if 0 <= score <= 100:
            self.grades[subject] = score
        else:
            print(f"Invalid score {score} for subject {subject}. Must be 0-100.")

    def calculate_average(self):
        if not self.grades:
            return 0
        total = sum(self.grades.values())
        return total / len(self.grades)

    def display_info(self):
        info = f"Name: {self.name}\nRoll Number: {self.roll_number}\nGrades:\n"
        for subject, grade in self.grades.items():
            info += f"  {subject}: {grade}\n"
        info += f"Average Grade: {self.calculate_average():.2f}"
        return info


class StudentTracker:
    def __init__(self):
        self.students = {}  # Store students by roll_number

    def add_student(self, name, roll_number):
        if roll_number in self.students:
            print(f"Student with roll number {roll_number} already exists.")
        else:
            self.students[roll_number] = Student(name, roll_number)

    def add_grade(self, roll_number, subject, score):
        student = self.students.get(roll_number)
        if student:
            student.add_grade(subject, score)
        else:
            print(f"No student found with roll number {roll_number}.")

    def get_student(self, roll_number):
        return self.students.get(roll_number)

    def calculate_class_average(self):
        if not self.students:
            return 0
        total = 0
        count = 0
        for student in self.students.values():
            avg = student.calculate_average()
            if avg > 0:
                total += avg
                count += 1
        return total / count if count > 0 else 0


# Example test code to run this file standalone
if __name__ == "__main__":
    tracker = StudentTracker()
    tracker.add_student("Alice", 1)
    tracker.add_student("Bob", 2)
    tracker.add_grade(1, "Math", 90)
    tracker.add_grade(1, "Science", 80)
    tracker.add_grade(2, "Math", 85)
    tracker.add_grade(2, "Science", 95)

    alice = tracker.get_student(1)
    print(alice.display_info())
    print()

    bob = tracker.get_student(2)
    print(bob.display_info())
    print()

    print(f"Class Average: {tracker.calculate_class_average():.2f}")
