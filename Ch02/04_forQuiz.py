fruits = ["apple", "banana", "cherry", "grape", "orange"]

fruit = input("과일을 영어로 입력해주세요 : ")

flag = False
for f in fruits:
    if fruit.lower() == f:
        print("과일이 있습니다.")
        flag = True
        break

if not flag:
    print("과일이 없습니다.")