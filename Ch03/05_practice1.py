def inputNumber():
    while True:
        try:
            order = input("Number : ")
            if order == "exit":
                print("Function Quit!")
                return '\0'
            num = int(order)
            return num
            
        except Exception as e:
            print("Wrong!! /", e)

print(inputNumber())