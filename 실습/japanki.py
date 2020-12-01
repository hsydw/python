print("자판기 관리 프로그램, 관리자 : 나효리, 111111")
print("=======================기능======================")
print("1 : 음료추가 2 : 음료삭제 3 : 자판기이용 4 : 종료")
print("=================================================")

drink = []
while True:  
    kineung = int(input("기능선택 : "))
    if kineung == 4:
        print("자판기 관리 프로그램 종료")
        break
    print("음료목록 :", drink)
    if kineung == 1:
        adddrink = input("추가할 음료는? ")       
        drink.append(adddrink)
        print("음료목록 :", drink)
    elif kineung == 2:
        deldrink = input("삭제할 음료는? ")
        drink.remove(deldrink)
        print("음료목록 :", drink)
    elif kineung == 3:
        money = int(input("동전을 넣으세요(500원 이상) : "))  
        while True:
            print("(현재 금액 : %d원) 음료 목록 :" %(money),drink )
            pick = int(input("음료를 선택하세요(순서대로 1, 2, 3... 입력, 거스름돈 받기: 0) : "))
            if pick == 0:
                print("거스름돈은 %d원 입니다." %(money))
                break 
            money = money - 500
            print("%s가 나왔습니다." %(drink[(pick-1)]))
            
                
    print("--------------------------")
