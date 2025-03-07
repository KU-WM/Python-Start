import random

class Student():
    def __init__(self, name='', id=int(random.randint(1, 100000)), major='', grade = 1):
        self.name = name
        self.id = id
        self.major = major
        self.korean = 0
        self.math = 0
        self.english = 0
        self.avg = 0
        if isinstance(grade, int):
            self.grade = grade
        else:
            try:
                grade = int(grade)
                self.grade = grade
            except:
                print("Grade Is Not Integer Or Integer String!")
    
    def showDetail(self):
        print(f"""이름: {self.name}, 학번: {self.id}, 전공: {self.major}, 학년: {self.grade}학년, 국어: {self.korean}, 수학: {self.math},영어: {self.english}, 평균: {self.avg}""")

    def inputScore(self, korean = 0, math = 0, english = 0):
        self.korean = int(korean)
        self.math = int(math)
        self.english = int(english)
        self.avg = (int(korean) + int(math) + int(english)) / 3
        
class StudentControl():
    def __init__(self):
        self.studentList = []

    def addStudent(self, student):
        if isinstance(student, Student):
            self.studentList.append(student)
        else:
            print("Wrong Input")

    def showStudentList(self):
        print("현재 등록된 학생 목록입니다.")
        print("===========================")
        for student in self.studentList:
            student.showDetail()
        print("===========================")

    def searchStudent(self, id):
        id = int(id)
        for student in self.studentList:
            if student.id == id:
                student.showDetail()
                break
    
    def editScore(self, id, subject, score):
        id = int(id)
        for student in self.studentList:
            if student.id == id:
                if subject == "korean":
                    student.avg = (student.avg * 3 - student.korean + int(score)) / 3
                    student.korean = int(score)
                elif subject == "math":
                    student.avg = (student.avg * 3 - student.math + int(score)) / 3
                    student.math = int(score)
                elif subject == "english":
                    student.avg = (student.avg * 3 - student.english + int(score)) / 3
                    student.english = int(score)
                else:
                    print("No Subject Matched")
                break

student1 = Student("홍길동", 1110, "도적학과", 3)
student1.inputScore(40, 70, 80)
student1.showDetail()
studentControl = StudentControl()

studentControl.addStudent(student1)
studentControl.showStudentList()
studentControl.searchStudent(1110)
studentControl.editScore(1110, "korean", 180)
studentControl.showStudentList()

sum([1, 3, 5])