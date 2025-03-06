try:
    name = input()
    if name.isalpha():
        print("WOW")
    else:
        print(1 % 0)
except:
    print("한글로 입력하세요")