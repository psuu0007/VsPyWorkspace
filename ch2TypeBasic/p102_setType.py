# 자바 set과 동일
# 재밌는건 set에 있는 데이터를 직접 접근하는 방법이 없다.(순서가 없어서 인덱스를 활용불가) 리스트나 튜플로 변환해야 접근할 수 있다
s1 = set([1, 2, 3])
print(s1)

s2 = set('Hello')
print(s2)

# set형변환
s1 = set([1, 2, 3])
listType = list(s1)
print(listType)

tupleType = tuple(s1)
print(tupleType)


# 103page 살펴보자
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

jkl = s2 - s1
print(jkl)

setType = set((1, 2, 3))
print(setType)
print(type(setType))
print(setType[0])