people = []
while True:
    name = input("Input Name: ")
    if not name.isalpha():
        print("Input Name in String!!")
        continue
    elif name == "exit":
        break

    people.append(name)

try:
    if len(people) >= 3:
        print(people[0], people[1])
except IndexError:
    print("Input More!")