# 리스트명 = [요소1, 요소2, 요소3, ...]

a = [1, 2, 3]
print(a)

print(a[-1])

a = [1, 2, 3,['a', 'b', 'c']]

print(a[3])
print(a[3][0])

# print(a[1][]) 오류가 난다 자바의 2차원 배열과는 역시 다르다. 뭔가 가변길이 배열 비슷하네



a = [1, 2, 3, 4, 5]
jkl = a[0:2]
print(jkl)

a = "12345"
jkl = a[:2]
print(jkl)

a = [1, 2, 3, 4, 5]
jkl = a[0:2]
print(jkl)

a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
jkl = f'30: {a[2:5]}'
print(jkl)

jkl = a[3][:2]
print(jkl)

#82page 부터 대충 참고하자
a = [1, 2, 3]
jkl = len(a)
print(jkl)

#숫자와 문자열을 연결해서 표현하고 싶으면 str()함수 방법도 있네
jkl = str(a[2]) + "hi"
print(jkl)

a = [1, 2, 3]
del a[1]
print(a)

a = [1, 2, 3, 4, 5]
del a[2:]
print(a)

#한번에 동일 행에 여러 값을 넣을 순 없지만 리스트를 넣는게 가능하네
a = [1, 2, 3]
a.append(4)
a.append([5, 6])
print(a)

#역순으로 정렬하는 것이 아니라 리스트를 거꾸로 뒤집는 개념이다
a = ['a', 'c', 'b']
a.reverse()
print(a) # 결과는 b c a



