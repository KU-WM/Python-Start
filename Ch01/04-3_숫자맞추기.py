import random

ans = False
num = random.randint(1, 100)
for i in range(6):
    temp = int(input("숫자를 입력해 주세요: "))
    if temp < num:
        print("더 큰수를 입력해주세요")
    elif temp > num:
        print("더 작은수를 입력하세요")
    else:
        print("정답입니다.")
        ans = True
        break
if not ans:
    print("기회가 전부 소진되었습니다.\n정답 :", num)
else:
    print("축하드립니다!!!")
print("종료")