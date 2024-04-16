""" 
1~100까지 합하였을 때 
100을 넘지 않는 가장 높은 숫자와 몇 번 숫자까지인지를 구하시오
"""


# sum = 0

# n = 1

# while n < 100:
#    sum = sum + n
#    if sum > 100:
#      print(f'1부터 {n-1}까지 더한 값: {sum-n}')
#      break
#    print(f'{n}번째 더한 값: {sum}')
#    n = n + 1
    

# while로 하니 
sum = 0

n = 1
numList = range(1, 101)
while n in numList: #여기가 true/false로만 인식하고 n에 값이 대입되지 않는다
   sum = sum + n
   if sum > 100:
     print(f'1부터 {n-1}까지 더한 값: {sum-n}')
     break
   print(f'{n}번째 더한 값: {sum}')
   

# for로 하니 
sum = 0

n = 1
numList = range(1, 101)
for n in numList: #대입이 생각한 대로 작동되네
   sum = sum + n
   if sum > 100:
     print(f'1부터 {n-1}까지 더한 값: {sum-n}')
     break
   print(f'{n}번째 더한 값: {sum}')