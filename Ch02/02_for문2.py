# 1 ~ 50까지의 수를 출력
# 2의 배수이면서 3의 배수
# 한줄에 5개까지의 숫자만 출력

count = 0
for i in range(1, 51):
    if i % 6 == 0:
        print(i, end=" ")
        count += 1
    if count == 5:
        print("\n", end="")
        count = 0

print("\n=================")

line = ""
count = 0
for i in range(1, 51):
    if i % 2 == 0 and i % 3 == 0:
        line = line + str(i) + " "
        count += 1
    if count == 5:
        print(line)
        line = ""
        count = 0
print(line)