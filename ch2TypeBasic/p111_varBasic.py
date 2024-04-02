a = 1
print(id(a))

b = a
print(a is b)

# 깊은 복사
listVar = [1, 2, 3]
otherList = listVar[:]
listVar[1] = 4
print(listVar)
print(otherList)

# 파이썬 모듈? 나중에 배운다고 하니 지금은 설명안하는게 좋겠네
from copy import copy
a = [1, 2, 3]
b = copy(a)
print(a is b) # False는 id가 다르기 때문

b = a.copy()
a[0] = 2
print(a)
print(b)

# 튜플 언패킹
a, b = ('py', 'life')
print(a)
print(type(a))
print(b)
print(type(b))

# 리스트 언패킹
a, b = ['py', 'life']
print(a)
print(b)

# 치환 대박이다 이딴식으로 변경하네?
a = 3
b = 5
print(a)
print(b)
a, b = b, a
print(a)
print(b)

