
"""
prompt = "''"

print('1. Add')
print('2. Del')
print('3. List')
print('4. Quit')

print("Enter number: ''")

"""


# 커피 자판기
coffee = 10
money = 0

while True:#무한루프 적용
    print("남은 커피의 양: %d개입니다.\n" % coffee)
    if coffee == 0:
        print("커피 품절")
        print("커피가 다 떨어졌습니다.")
        break
    
    money = int(input("돈을 넣어 주세요"))
    if money == 300:
        coffee = coffee - 1
        print("커피가 나왔습니다")
    elif money > 300:
        coffee = coffee - 1
        print("거스름돈 %d원 입니다" %(money-300))
        print("커피가 나왔습니다")
    elif money == 0:
        print("\n자판기 이용종료")
        break
    elif money < 300:
        print("금액이 부족합니다")
        print("부족한 금액: %d원" %(300-money))
    print()
