# 매개변수 초기화

def sayMySelf(name, age, man=True):
    print("나의 이름은 %s 입니다." %name)
    print("나이는 %d살 입니다." %age)
    if man:
        print("남자입니다")
    else:
        print("여자입니다")




sayMySelf("홍길동", 27)

sayMySelf("달래", 26, False)

# 167참고
# 매개변수 초기화가 있다면 앞이나 중간에 작성이 불가능함 
# 초기화하고 싶은 매개변수는 항상 뒤에서 꼭 채워야 함
# def sayMySelf(name, man=True, age):
#     print("나의 이름은 %s 입니다." %name)
#     print("나이는 %d살 입니다." %age)
#     if man:
#         print("남자입니다")
#     else:
#         print("여자입니다")
