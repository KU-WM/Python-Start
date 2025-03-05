students = []
flag = True

while flag:
    print("\n메뉴를 입력하세요\n1. 학생등록 \n2. 학생목록출력 \n3. 학생검색 \n4. 성적평균계산 \n5. 우수학생선발 \n6. 과목우수자 \n7. 성적수정 \n8. 종료\n================================\n")
    command = int(input())
    if command == 1:
        # 학생 등록
        students.append({"이름":input("학생 이름을 입력해 주세요: "), "학번": input("학생 학번을 입력해 주세요: "), 
                         "국어성적": int(input("학생의 국어성적을 입력해 주세요: ")), 
                         "수학성적": int(input("학생의 수학성적을 입력해 주세요: ")), 
                         "영어성적": int(input("학생의 영어성적을 입력해 주세요: "))})
        
    elif command == 2:
        # 학생목록
        for student in students:
            print(student)

    elif command == 3:
        # 학생검색
        search = input("검색할 학생의 학번을 입력해주세요 : ")
        found = False
        for student in students:
            if student["학번"] == search:
                print(f"{student['이름']}의 성적은 국어: {student['국어성적']}점 수학: {student['수학성적']}점 영어: {student['영어성적']}점 입니다.")
                found = True
                break
        if not found:
            print("해당하는 학생은 존재하지 않습니다.")

    elif command == 4:
        # 성적평균
        for student in students:
            print(f"{student['이름']}학생의 성적 평균은 {(student['국어성적'] + student['수학성적'] + student['영어성적']) / 3}점 입니다.")

    elif command == 5:
        # 우수학생
        for student in students:
            if (student["국어성적"] + student["수학성적"] + student["영어성적"]) / 3 >= 80:
                print(f"{student['이름']}학생", end=" ")
        print("은 우수 학생입니다.")

    elif command == 6:
        # 과목우수자
        search = input("조회할 과목명을 입력해 주세요 (국어, 수학, 영어): ")
        scoreTemp = []
        for student in students:
            scoreTemp.append(student[search + "성적"])
        score = max(scoreTemp)
        for student in students:
            if student[search + "성적"] == score:
                print(f"{student['이름']}학생, ", end="")
        print("이 최고점을 받았습니다.")

    elif command == 7:
        # 성적수정
        search = input("검색할 학생의 학번을 입력해주세요 : ")
        found = False
        for student in students:
            if student["학번"] == search:
                search = input("수정할 과목명을 입력해 주세요 (국어, 수학, 영어): ")
                score = int(input("수정할 점수를 입력해 주세요: "))
                student[search + "성적"] = score
                print("수정이 완료되었습니다.")
                found = True
                break
        if not found:
            print("해당하는 학생은 존재하지 않습니다.")
        

    elif command == 8:
        # 종료
        flag = False
    else:
        print("잘못된 입력입니다.")

print("종료되었습니다.")