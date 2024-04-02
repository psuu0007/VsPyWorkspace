# 파이썬에서는 true, false는 예약어가 아니다. 
# True, False처럼 첫글자를 대문자로 작성해야한다

a = True
# b = false #오류 발생

print(type(a))

print(1 != 1)

# 107page 자료형의 참과 거짓 참고
 
if 'python':
    print('python')
else:
    print(False)

if '':
    print('따옴표')
else:
    print(False)

if [1, 2, 3]:
    print('[1, 2, 3]')
else:
    print(False)

if []:
    print('[]')
else:
    print(False)

if ():
    print('()')
else:
    print(False)

if {'a', 1}:
    print('{"a", 1}')
else:
    print(False)

if 1:
    print(1)
else:
    print(False)

if 0:
    print(0)
else:
    print(False)

if None:
    print(None)
else:
    print(False)

# 이 특징을 활용한 예 vscode에서는 무한루프시 ctrl + F5누르면 디버깅 모드를 중단할 수 있다
# pop()을 사용하는건 이터레이터 패턴인 경우네
numList = [1, 2, 3, 4]
while numList:
    print(numList.pop())

# 참, 거짓 판별
jkl = bool('p')
print(jkl)



