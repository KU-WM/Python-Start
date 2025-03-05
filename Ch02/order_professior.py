menus = {
    "메뉴1": 1000,
    "메뉴2": 2000,
    "메뉴3": 3000,
    "메뉴4": 4000,
    "메뉴5": 5000
}

print("\n=== 메 뉴 ===")

for name, price in menus.items():
    print(f"{name} - {price}원");

orders = {}

while True:
    menu_name = input("주문할 메뉴를 입력하세요: ")
    exist = False

    if menu_name in menus:
        print("exists in menus")
        exist = True
        quantity = int(input("수량을 입력하세요 : "))
        if menu_name in orders:
            print("exist in orders")
            orders[menu_name] += quantity
        else:
            print("new")
            orders[menu_name] = quantity
    
    if not exist:
        print("메뉴가 존재하지 않습니다.")

    more = input("추가 주문 하시겠습니까? (y/n): ")
    if more.lower() == "n":
        break

total_price = 0
total_quantity = 0
print("\n=== 주문 내역 ===")
for item, qty in orders.items():
    discount_qty = qty // 3
    discounted_price = menus[item] * (qty - discount_qty)
    price = menus[item] * qty
    # total_price += price
    total_price += discounted_price
    total_quantity += qty
    if discount_qty > 0:
        print(f"{item}: {qty}개 - {price}원 ({discount_qty}개 무료)")
    else:
        print(f"{item}: {qty}개 - {price}원")

if total_price >= 10000:
    total_price *= 0.9
    print("10% 할인 적용됨")

print(f"최종 주문 금액: {total_price}원")