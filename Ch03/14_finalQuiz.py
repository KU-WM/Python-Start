def genderCount(datas):
    m = 0
    for data in datas:
        if data[2] == "Male":
            m += 1
    print(f"Male: {m}, Female: {len(datas) - m}")

try:
    datas = []
    with open("raw_data.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        datas = list(li.split(",") for li in list(line.split("\n")[0] for line in lines))

    print(datas)
    with open("filtered_data.txt", "w") as file:
        for data in datas:
            if int(data[1]) >= 18:
                file.write(data[0] + "," + data[1] + "," + data[2] + "\n")

    genderCount(datas)
            
except Exception as e:
    print(e)