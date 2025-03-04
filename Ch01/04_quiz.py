score = int(input("성적을 입력하세요: "))
print("A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F", "학점" ,sep="")