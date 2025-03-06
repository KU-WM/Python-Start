def load_file():
    with open('콘텐츠_소비.csv', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for idx, line in enumerate(lines):
            # if idx > 24:
            #     break
            line = line.split(",")
            line = list(li for li in line if li != "" and li != "\n")
            print(idx, ":", line)
    return 0