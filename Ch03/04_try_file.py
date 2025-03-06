try :
    names = []
    file = open("person.txt", "rt", encoding="utf-8")
    while True:
        name = file.readline()
        if name:
            names.append(name.split("\n")[0])
        else:
            break
    
    print(names)
except Exception as e:
    print("Error: ", e)
finally:
    try:
        file.close()
    except :
        print("Error")