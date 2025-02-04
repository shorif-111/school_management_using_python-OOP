class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.teachers = {}
        self.classrooms = {}
    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom
    def add_teacher(self, subject, teacher):
        self.teachers[subject] = teacher
    def admission(self, student):
        class_name = student.classroom.name
        self.classrooms[class_name].add_student(student)
    def calculate_grade(self, marks):
        if marks>=80 and marks<=100:
            return "A+"
        elif marks>=70 and marks<80:
            return "A"
        elif marks>=60 and marks<70:
            return "B"
        elif marks>=50 and marks<60:
            return "C"
        elif marks>=40 and marks<50:
            return "D"
        else:
            return "F"
    def grade_to_value(grade):
        if grade=="A+":
            return 5.00
        elif grade=="A":
            return 4.00
        elif grade=="A-":
            return 3.50
        elif grade=="B":
            return 3.00
        elif grade=="C":
            return 2.00
        elif grade=="D":
            return 1.00
        else:
            return 0.00
    def value_to_grade(value):
        if value==5.00:
            return "A+"
        elif value>=4.00 and value<5.00:
            return "A"
        elif value>=3.50 and value<4.00:
            return "A-"
        elif value>=3.00 and value<3.50:
            return "B"
        elif value>=2.00 and value<3.00:
            return "C"
        elif value>=1.00 and value<2.00:
            return "D"
        else:
            return "F"


class School:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        self.teachers = {} # {"bangla" : teacher_object}
        self.classrooms = {} # {"eight" : classroom_object}
    
    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom
    def add_teacher(self, subject, teacher):
        self.teachers[subject] =  teacher
    def student_admission(self, student):
        classname = student.classroom.name
        self.classrooms[classname].add_student(student)
    
    # rahim - bang - 50 - B - 2.00
    #       - eng  - 80 - A+ - 5.00
    # ------------------------
    # total ----------- - C - 2.00
    @staticmethod
    def calculate_grade(marks):
        if marks>=80 and marks<=100:
            return 'A+'
        elif marks >= 70 and marks<80:
            return 'A'
        elif marks >= 60 and marks <70:
            return 'A-'
        elif marks >= 50 and marks <60:
            return 'B'
        elif marks >= 40 and marks < 50:
            return 'C'
        elif marks >= 33 and marks < 40:
            return 'D'
        else:
            return 'F'
    @staticmethod
    def grade_to_value(grade):
        grade_map = {
            'A+' : 5.00,
            'A' : 4.00,
            'A-' : 3.50,
            'B' : 3.00,
            'C' : 2.00,
            'D' : 1.00,
            'F' : 0.00
        }
        return grade_map[grade]
    
    @staticmethod
    def value_to_grade(value):
        if value >=4.5 and value<=5.00:
            return 'A+'
        elif value >= 3.5 and value <4.50:
            return 'A'
        elif value >= 3.0 and value < 3.5:
            return 'A-'
        elif value >= 2.5 and value < 3.0:
            return 'B'
        elif value >= 2.0 and value < 2.5:
            return 'C'
        elif value >= 1.0 and value < 2.0:
            return 'D'
        else:
            return 'F'
    
    def __repr__(self):
        # All Classrooms
        for key in self.classrooms.keys():
            print(key)
        # All Students
        print("All Students")
        result = ''
        for key,value in self.classrooms.items(): # prottekta classroom e gelam
            result += f"---{key.upper()} Classroom Students\n"
            for student in value.students:
                result += f"{student.name}\n"
        print(result)
        # All Subjects
        subject = ''
        for key,value in self.classrooms.items(): # prottekta classroom e gelam
            subject += f"---{key.upper()} Classroom Subjects\n"
            for sub in value.subjects:
                subject += f"{sub.name}\n"
        print(subject)
        # All Teachers - Homework
        # All Student Results
        print("Students Results")
        for key,value in self.classrooms.items():
            for student in value.students:
                for k,i in student.marks.items():
                    print(student.name,k,i,student.subject_grade[k])
                print(student.calculate_final_grade())
        return ''
                