a = 3
if a > 1:
    print("a는 1보다 크다")
# 공백 스페이스는 꼭 4칸이 아니라도 실행엔 문제가 없지만 일관성, 가독성을 위해 무조건 탭의 구성과 맞춰주자
    
print("a의 타입은 ") 
print(type(a))

a = 0o30
print(a)
print(type(a))


a = 3
b = 4
print(a / b) #정수 나누기는 실수 float
print(type(a/b))

#자바처럼 몫이 나오려면
print(a // b)

print(a % b)

print(a ** b) #a의 b제곱