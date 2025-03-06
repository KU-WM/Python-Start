with open('data.txt', "r", encoding='utf-8') as file:
    count = 1
    lines = file.readlines()
    for line in lines:
        print(count, " : ", line, sep="")
        count += 1
    for idx, line in enumerate(lines):
        print(idx, ":", line)

    # print(x for x in lines)