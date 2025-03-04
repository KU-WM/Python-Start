flag = True
id = input("아이디를 입력해 주세요: ")
password = input("비밀번호를 입력해주세요: ")
isLogin = False
count = 0

try:
    balance = 100000
    balance2 = 100000
    log = []

    while(flag):
        if not isLogin:
            tempId = input("아이디: ")
            tempPass = input("비밀번호: ")
            if tempId == id and tempPass == password:
                isLogin = True
                print("로그인 되었습니다.")
            else:
                print("잘못 입력하셨습니다.")
                count += 1
                if count > 2:
                    break
                else:
                    continue
        
        print("\n------------------------------")
        print("1. 입금\n2. 출금\n3. 잔액조회\n4. 송금\n5. 로그\n6. 종료\n------------------------------")
        commend = int(input("원하시는 메뉴를 입력해 주세요 : "))
        if(commend == 1):
            # add
            money = int(input("입금 금액을 입력해 주세요 : "))
            if money <= 0:
                print("입금은 0보다 작을 수 없습니다.")
                continue
            balance += money
            print("입금이 완료되었습니다.")
            if len(log) > 4:
                del log[0]
            log.append(["입금 : ", money])
            continue

        elif(commend == 2):
            # sub
            money = int(input("출금 금액을 입력해 주세요 : "))
            if money <= 0:
                print("출금은 0보다 작을 수 없습니다.")
                continue
            if balance < money:
                print("잔액이 모자랍니다.")
                continue
            balance -= money
            print("출금이 완료되었습니다.")
            if len(log) > 4:
                del log[0]
            log.append(["출금 : ", money])
            continue

        elif(commend == 3):
            # print
            print("잔액은 %d원 입니다." %balance)

        elif(commend == 4):
            # sub
            money = int(input("송금 금액을 입력해 주세요 : "))
            if money <= 0:
                print("송금은 0보다 작을 수 없습니다.")
                continue
            if balance < money:
                print("잔액이 모자랍니다.")
                continue
            balance -= money
            balance2 += money
            print("송금이 완료되었습니다.")
            if len(log) > 4:
                del log[0]
            log.append(["송금 : ", money])
            continue

        elif(commend == 5):
            for i in range(5):
                print(i + 1, "> ", log[i][0], log[i][1], "원", sep="")
            continue

        elif(commend == 6):
            # quit
            flag = False
            continue

        else:
            print("잘못된 입력입니다.\n1 ~ 4의 숫자를 입력해주세요.")

except ValueError:
    print("잘못된 입력입니다.")