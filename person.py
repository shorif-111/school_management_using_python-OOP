from random import randint
from school import School

class Person:
    def __init__(self, name):
        self.name = name
       

class Student(Person):
    def __init__(self, name, classrooom):
        super().__init__(name)
        self.classroom = classrooom
        self.__id = None
        self.grade = None
        self.marks = {}
        self.subjects_grade = {}
    def calculate_final_grade(self):
        total = 0
        for grade in self.subjects_grade.values():
            point = School.grade_to_value(grade)
            total += point
        if total == 0:
            gpa = 0
            self.grade = 'F'
        else:
            gpa = total/len(self.subjects_grade)
            self.grade = School.value_to_grade(gpa)
        return f"{self.name} Final Grade : {self.grade} with GPA = {gpa}"
        
    

class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)
    def Evaluate_exam(self):
        return randint(1, 100)

@property
def id(self):
    return self.__id
@id.setter
def id(self, id):
    self.__id = id