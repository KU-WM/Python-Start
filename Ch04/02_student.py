from datetime import datetime

# 출석부 명단(리스트)
students = ["홍길동", "장길산", "임꺽정"]

# 출석현황(금일, 딕셔너리)
attendance = {}

# 출석체크(for)
for student in students:
    status = input(f"{student}(1:출석/2:결석): ")
    if status.lower() == "1":
        attendance[student] = "O"
    else:
        attendance[student] = "X"

# 통계
total_students = len(students)   #총인원
present_count = sum(1 for status in attendance.values() if status == "O")   #출석한 인원
absent_count = total_students - present_count #결석한 인원

# 오늘 날짜 계산
today = datetime.today()
formatted_today = today.strftime("%Y-%m-%d")

# 요일 숫자 (월=0, 화=1, ... 일=6)
weekday_num = today.weekday()
# 요일을 한글로 출력
days_korean = ["월", "화", "수", "목", "금", "토", "일"]
weekday = days_korean[weekday_num]

# 출력
print("금일 전체 출결현황")
print(attendance)

print("서울 휴먼교육센터")
print(f"{formatted_today} ({weekday})")     # 오늘 날짜 출력
print("1교시 : 3교육실")
print(f"총인원 : {total_students}")         # 실제 총원  
print("Hrd출석 : -")
print(f"교실출석 : {present_count}")       # 실제 출석 인원
print("지각: -")
print(f"결석: {absent_count}")             # 실제 결석 인원
print("조퇴: -")
