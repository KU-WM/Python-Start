try:
    num = int(input("nmumber: "))
    print(num)
except:
    print("Input Correct Number!asd")

try:
    num1 = int(input("nmumber 1: "))
    num2 = int(input("nmumber 2: "))

    print(num1 / num2)
except ValueError:
    print("TypeError / Input Number")
except ZeroDivisionError:
    print("ZeroDivisionError")

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
