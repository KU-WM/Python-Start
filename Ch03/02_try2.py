try:
    file = open("data.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
finally:
    try:
        file.close()
    except NameError:
        print("NameError")
