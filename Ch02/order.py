menu = {"menu1": 1000, "menu2": 2000, "menu3": 3000, "menu4": 4000, "menu5": 5000}

orderlist = [0, {}]

print("===== MENU =====")
for key, value in menu.items():
    print(f"{key} - {value}원")
print("================\n")

while True:
    order = input("주문할 메뉴를 입력하세요 : ")
    # order in menu.keys() <= keys() 안해줘도 됨
    if order in menu:
        num = int(input("수량을 입력하세요 : "))
        orderlist[0] += menu[order] * num
        if order in orderlist[1]:
            orderlist[1][order] = orderlist[1][order] + num
        else:
            orderlist[1][order] = num
    else:
        print("존재하지 않는 메뉴입니다. 다시 입력해 주세요.\n")

    if input("추가 주문하시겠습니까? (y/n)").lower() == "n":
        break

print("주문이 완료되었습니다.")
print(orderlist)
log = []

print("======== 주문 내역 ========")
for key, value in orderlist[1].items():
    if value > 2:
        orderlist[0] -= menu[key] * (value // 3)
        log.append(key)
    print(f"{key} : {value}개 - {menu[key] * value}원")

if orderlist[0] < 10000:
    print(f"총액 {orderlist[0]}")
    
else:
    print(f"총액 {orderlist[0] * 0.9}")
    log.append("10%")

for i in range(len(log)):
    if log[i] == "10%":
        print("10% 할인 적용됨")
    else:
        print(f"{log[i]} 3개이상 구매로 1개 무료")