""" 
*
**
***
****
*****
"""

# n = 0
# while n < 5: 
#    kindCnt = 0
#    while kindCnt <= n:
#       print('*', end="")
#       kindCnt = kindCnt + 1
#    print()
#    n = n + 1



# 반쪽 다이아몬드 (while 루프)
i = 0
while i < 5:
    print(' ' * (5-(i+1)) + '*' * (i + 1))
    i += 1

# 역반쪽 다이아몬드 (while 루프)
i = 5
while i > 0:
    print(' ' * (5-i) + '*' * (i))
    i -= 1
   


# # 정방향 다이아몬드
# for i in range(6):
#     print(' ' * (5 - i) + '*' * (i * 2 + 1))

# # 역방향 다이아몬드
# for i in range(6):
#     print(' ' * i + '*' * (11 - (2 * i)))



