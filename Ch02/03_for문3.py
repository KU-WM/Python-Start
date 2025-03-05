animals = ["강아지", "고양이", "다람쥐"]

for animal in animals:
    print(animal)

for i in range(len(animals)):
    print(animals[i])

# enumerate: 리스트의 인덱스와 내용물을 반환
# print(f"{x}"): {}안에 x라는 변수 출력 가능, {}없으면 문자열 그대로 출력
for index, animal in enumerate(animals):
    print(f"{index}: {animal}")