students = [] 
while True: 
    name = input("학생 이름: ") 
    age = int(input("나이: ")) 
    major = input("전공: ") 
    students.append({"이름": name, "나이": age, "전공": major})
    if len(students) > 2:
        print("Max Student  is 3!!")
        break
    if input("계속 입력하시겠습니까? (y/n): ") == 'n': 
        break

for student in students:
    if student["나이"] > 20:
        print(student["이름"], "님 ", student["나이"], "세 ", student["전공"], sep="")

########################################################################################
flag = False
search = input("검색할 이름을 입력해주세요 : ")
for student in students:
    if student["이름"] == search:
        print(student)
        flag = True
        break

if not flag:
    print("해당하는 학생은 없습니다.")

#########################################################################################
flag = False
search = input("검색할 이름을 입력해주세요 : ")
for student in students:
    if student["이름"] == search:
        print(student)
        flag = True
        print("학생을 찾았습니다.")
        ch1 = input("변경할 분류 입력 : ")
        ch2 = input("변경할 정보 입력 : ")
        student[ch1] = ch2
        print("수정되었습니다.")
        print(student)
        