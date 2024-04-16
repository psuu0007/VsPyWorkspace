
def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

# 기본적으로 튜플로 전달이 되는데
result = add_many(1, 2, 3)
print(result)


nums = [2, 3, 4]
# 리스트를 전달하려면 *를 붙여야 하네;
result = add_many(*nums)
print(result)


""" 
nums = [2, 3, 4]
result = add_many(nums)
print(result)

이런식으로 i값을 정수랑 더하지 않으면 인자에 *이 없어도 별 문제가 없네
def add_many(*args):
    result = 0
    for i in args:
        print(i)
    return result

 """

# 161페이지는 좀 신기하긴 하네 참고하자
