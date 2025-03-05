fruits = ["사과", "바나나", "체리"]

fruits.append("포도")
fruits.remove("바나나")
fruits[1] = "블루베리"

print(fruits)

person = {"이름":"김철수", "나이":25}
person["지역"] = "서울"

print(person)

students = []
students.append({'이름': '홍길동', '나이': 20, '학번': '2024001'})
students.append({'이름': '이영희', '나이': 22, '학번': '2024002'})
students.append({'이름': '박철수', '나이': 21, '학번': '2024003'})

for student in students:
    print(student)