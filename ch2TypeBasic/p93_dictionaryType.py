dic = {'name' : 'pey', 'phone' : '010-9999-1234', 'birth' : '1118'}

print(dic)
print(dic['name'])

# 딕셔너리 값 추가
dic[2] = 'two'
print(dic)

# dic['2'] = 2
# print(dic)

#딕셔너리 값 삭제
del dic[2]
print(dic)


#키가 중복되면 Map처럼 마지막 key 값으로 대체된다(중복 X)
# 97~98p 딕셔너리 특징도 참고하자(list와 tuple 관련)

dic = {'name' : 'pey', 'phone' : '010-9999-1234', 'birth' : '1118'}
jkl = dic.keys() #키 데이터만 가져오기
print(jkl)

jkl = dic.values()
print(jkl)

jkl = dic.items()
print(jkl)
print(type(jkl))


# key로 value 얻기 get함수
# 일반적인 ['키'] 방식과 get('키') 방식의 존재하지 않는 키 접근시 차이점
# None와 에러 발생
dic = {'name' : 'pey', 'phone' : '010-9999-1234', 'birth' : '1118'}
jkl = dic.get('nokey')
print(jkl)
# jkl = dic['nokey'] #에러가 발생함
# print(jkl)

jkl = dic.get('nokey', '키가 존재하지 않음')
print(jkl)

# 해당 key가 딕셔너리 안에 있는지 조사 in
jkl = 'name' in dic
print(jkl)
jkl = 'email' in dic
print(jkl)