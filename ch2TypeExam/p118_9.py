""" 딕셔너리의 키
다음 중 오류가 발생하는 경우를 고르고, 
그 이유를 설명하시오 """

# 자바스크립트랑은 좀 다름 변수 선언 및 초기화는 해야 값을 넣을 수 있음
# a = dict()
a = {}

a['name'] = 'py1'
print(a)
a[('a', )] = 'py2'
print(a)
# a[[1]] = 'py3'
# print(a)
a[250] = 'py4'
print(a)


# print(a.keys('name'))


my_dict = {'name': 'py1', ('a',): 'py2', 250: 'py4'}

# 키만 출력
for key in my_dict.keys():
    print(key)

# 'name' 키의 값 출력
print("Name:", my_dict['name'])