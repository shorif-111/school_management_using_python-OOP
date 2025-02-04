from school import School
from person import Teacher

class Subject:
    def __init__(self, name, techer):
        self.name = name
        self.teacher = techer
        self.max_marks = 100
        self.max_marks = 33
    def exam(self, students):
        for student in students:
            marks = self.teacher.Evaluate_exam()
            student.marks[self.name] = marks
            student.subjects_grade[self.name] = School.calculate_grade(marks)
        