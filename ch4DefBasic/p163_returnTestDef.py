# 함수의 리턴값은 언제나 하나이다

def addAndMul(a, b):
    return a+b, a*b

result = addAndMul(3, 4)
print(result)


result = result + (1, 2)

print(result)


result1, result2 = addAndMul(3, 4)
print(result1)
print(result2)

# 이게 오류가 아닌게 자바랑 좀 다르고 위에 return이 남네
def addAndMul(a, b):
    return a+b
    return a*b

a = addAndMul(3, 4)
print("리턴 두번 정의된 함수결과: %d" %a)



original_tuple = (1, 7)
modified_list = list(original_tuple)
modified_list[0] = 2
modified_list[1] = 8
new_tuple = tuple(modified_list)
print(new_tuple)  # 출력: (2, 8)

list1 = [1, 7]
list2 = [1, 1]
other_list = list1 + list2
print(other_list)  # 출력: [1, 7, 1, 1]


# 특이하긴 하네 리스트도 배열이기 때문에 직접 사칙연산은 불가능하다
# +는 추가의 개념
my_list = [1, 2, 3, 4]
other_list = [10, 20, 30, 40]
new_list = []

for item in my_list:
    new_item = [item * num for num in other_list] # 각 요소를 두 배로 만듦
    new_list.append(new_item)  # 새로운 리스트에 추가

print(new_list)  # 출력: [2, 14, 6, 10]

my_list = [1, 2, 3, 4]
other_list = [10, 20, 30, 40]
new_list = []

for item in my_list:
    i = 0
    new_item = item * other_list[i]
    new_list.append(new_item)  # 새로운 리스트에 추가
    i += 1

print(new_list)  # 출력: [2, 14, 6, 10]

