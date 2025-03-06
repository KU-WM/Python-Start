import csv

data = [["이름", "나이", "전공"],
        ["홍길동", 20, "컴퓨터공학"],
        ["이순신", 22, "기계공학"]]

with open("student.csv", "w", newline="", encoding='cp949') as file:
    writer = csv.writer(file)
    writer.writerows(data)