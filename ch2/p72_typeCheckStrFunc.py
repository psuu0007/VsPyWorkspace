a = 'hobby'
resultStr = f'문자 개수 세기: {a.count("b")}'
print(resultStr)

a = '파이썬은 최고의 선택이다'
resultStr = f'위치 알려주기: {a.find("택")}'
print(resultStr)


#중요한가 봄 리스트와 튜플에서 사용된다고 하니
a = 'abcd'
resultStr = ",".join('abcd')
print('문자열 삽입: ' + resultStr)

# 74page에 그냥 대충 다아는거 있음

a = 'Life is too short'
resultStr = a.replace('short', 'hard')
print('문자열 바꾸기: ' + resultStr)

# 문자열 나누기 split의 결과값은 리스트 자료형으로 반환된다
a = 'Life is too short'
print(a.split())

b = 'a:b:c:d'
resultStr = b.split(':')
print(resultStr)