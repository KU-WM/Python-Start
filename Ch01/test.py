flag = True

try:
    balance = int(input("초기 자본을 입력하세요 : "))

    while(flag):
        print("\n------------------------------")
        print("1. 입금\n2. 출금\n3. 잔액조회\n4. 종료\n------------------------------")
        commend = int(input("원하시는 메뉴를 입력해 주세요 : "))
        if(commend == 1):
            # add
            money = int(input("입금 금액을 입력해 주세요 : "))
            balance += money
            print("입금이 완료되었습니다.")
            continue

        elif(commend == 2):
            # sub
            money = int(input("출금 금액을 입력해 주세요 : "))
            if balance < money:
                print("잔액이 모자랍니다.")
                continue
            balance -= money
            print("출금이 완료되었습니다.")
            continue

        elif(commend == 3):
            # print
            print("잔액은 %d원 입니다." %balance)
            continue

        elif(commend == 4):
            # quit
            flag = False
            continue

        else:
            print("잘못된 입력입니다.\n1 ~ 4의 숫자를 입력해주세요.")

except:
    print("잘못된 입력입니다.")