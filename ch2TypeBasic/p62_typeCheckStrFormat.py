a = "I eat %d apples." % 3
print(a)

b = "I eat " + str(3) + " apples" # b방식보다 a방식으로 사용하는게 편하다 명칭은 문자열 포매팅이라고 한다(문자열 안에 어떤 값을 삽입하는 방법)
print(b)

# c = "I eat " + 3 + " apples" # 문자열로 자동으로 변환이 안되네 오류가 난다
# print(c)


# %d는 숫자 대입
# %s는 문자열 대입: 문자열의 경우 % 문자열 표기인 따옴표를 넣어야 한다
d = "I eat %s apples." % "five"
print(d)


#66페이지 내용 참고
str = 'hi'
e1 = "%10sjane." % str
e2 = "%-10sjane." % str
print(e1)
print(e2)

#반올림으로 작동하나 보네, 소수점 4자리 표현인데 그 뒤에 자리수에서 반올림이 되고 있음
f = "%10.4f" % 3.1234567
print(f)

#포매팅 함수: '문자열 {대입할 문자 번호 위치}'.format(문자열) 
g1 = 'g1->I eat {0} apples'.format("five")
g2 = 'g2->I eat {0} apples'.format(1+2)
print(g1)
print(g2)
num = 10
day = 'three'
g3 = 'g3->I eat {0} apples. so I was sick for {1} days.'.format(num, day)
print(g3)

#이름으로 넣기 이 방식이 나쁘지 않아 보이네?
g4 = 'g4->I eat {num} apples. so I was sick for {day} days.'.format(num=5, day='삼')
print(g4)
g5 = 'g5->{0:<10}'.format('왼쪽 정렬')
print(g5)
g6 = 'g6->{str:>10}'.format(str='오른쪽 정렬')
print(g6)
g7 = 'g7->{str:^10}'.format(str='가운데 정렬')
print(g7)
g8 = 'g8->{str:=^10}'.format(str='공백 채우기')
print(g8)
g9 = 'g9->{str}'.format(str='{중괄호 인식}')
print(g9)

#71page f문자열 포매팅
name = '홍길동'
age = 30
str = f'나는 내년이면 {age + 1}살이 된다'
print(str)

d = {'name' : '홍길동', 'age' : 30}
str = '나는 내년이면 {name}이 된다'.format(name=d['age'])
print(str)

