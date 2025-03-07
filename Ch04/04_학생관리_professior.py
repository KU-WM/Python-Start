class Student():
    def __init__(self, name, student_id, major, year):
        self.name = name
        self.student_id = student_id
        self.major = major
        self.year = year

    def display_info(self):
        print("---------------------------")
        print(f"학번: {self.student_id} | 이름: {self.name} | 전공: {self.major} | 학년: {self.year}")



# Student 상속
class StudentWithScores(Student):
    def __init__(self, name, student_id, major, year):
        # 부모의 생성자를 가져와서 실행
        super().__init__(name, student_id, major, year)
        self.grades = {}
        self.avg = 0

    def display_info(self):
        super().display_info()
        for k, v in self.grades.items():
            print(f"{k} : {v}")
        print(f"avg:", self.avg, "|", f"MAX: {max(self.grades.values() if self.grades.values() else [0])} | MIN: {min(self.grades.values() if self.grades.values() else [0])}")
        print("---------------------------")

    def getAvarageScore(self):
        return round(self.getTotalScore() / len(self.grades.keys()), 2)
    
    def getTotalScore(self):
        return sum(self.grades.values())

    def getMaxScore(self):
        return max(self.grades.values())
    
    def getMinScore(self):
        return min(self.grades.values())

    def addGrade(self, subject, score):
        if not 0 <= score <= 100:
            print("Score is out of Range!")
            return 0
        
        if subject in self.grades.keys():
            print("Input Subject Is Already Exist!")
            return 0

        self.grades[subject] = int(score)
        self.avg = round((sum(sc for sc in self.grades.values())) / len(self.grades.keys()), 2)
        for k, v in self.grades.items():
            print(f"{k} : {v}")
        print("avg :", self.avg)
    
    def addGrades(self, dict):
        self.grades.update(dict)
        self.avg = round((sum(sc for sc in self.grades.values())) / len(self.grades.keys()), 2)
        for k, v in self.grades.items():
            print(f"{k} : {v}")
        print("avg :", self.avg)

    def editGrade(self, subject, score):
        if not subject in self.grades.keys():
            print("Input Subject Is Not Found!")
            return 0
        
        self.grades[subject] = int(score)
        self.avg = round((sum(sc for sc in self.grades.values())) / len(self.grades.keys()), 2)
        for k, v in self.grades.items():
            print(f"{k} : {v}")
        print("avg :", self.avg)
    


student1 = StudentWithScores("홍길동", "1111", "빅데이터", "1학년")
student1.addGrade("korean", 23)
scores = {"math": 12, "english": 88}
student1.addGrades(scores)

student2 = StudentWithScores("장발장", "2222", "객체지향", "3학년")
student2.addGrade("korean", 73)
scores = {"math": 92, "english": 68}
student2.addGrades(scores)

student1.editGrade("SCFF", 777)
student1.editGrade("korean", 76)

student1.display_info()
student2.display_info()