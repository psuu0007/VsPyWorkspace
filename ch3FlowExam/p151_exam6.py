""" 
리스트의 요소 중 홀수만 골라 2를 곱한 값을
result 리스트에 할당하시오
"""

numbers = [1, 2, 3, 4, 5]


result = [num * 2 for num in numbers if num%2 == 1]

# 홀수는 1, 3, 5
print(result)


