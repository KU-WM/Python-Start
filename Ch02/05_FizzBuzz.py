# FizzBuzz

for i in range(1, 51):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


# 입력받은 두 수 사이의 값의 합

sum = 0
while 1:
    n1 = int(input("Input first num: "))
    n2 = int(input("Input second num: "))

    n1, n2 = (n1, n2) if n1 < n2 else (n2, n1)

    for i in range(n1 + 1, n2):
        sum += i
    #sum = sum(range(n1 + 1, n2))
    if sum > 0:
        break
    else:
        print("다시 입력해 주세요. 합이 0 초과여야 합니다.")
        sum = 0
    
print(sum)