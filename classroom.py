from school import School

class Classroom:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.subjects = []
    def add_student(self, student):
        self.students.append(student)
    def add_subject(self, subject):
        self.subjects.append(subject)
    def take_semester_final(self):
        for subject in self.subjects:
            subject.exam(self.students)
        for student in self.students:
            student.calculate_final_grade()
    
